import argparse
import os
import pathlib
from typing import Tuple
import time
# mifare classic 4b uid binary to flipper .nfc converter. 
# Created by Equipter with code portions borrowed from Lucaslhm/AmiiboFlipperConverter
# V1.06


def write_output(name: str, assemble: str, out_dir: str):
    with open(os.path.join(out_dir, f"{name}.nfc"), "wt") as f:
        f.write(assemble)


def convert(contents: bytes) -> Tuple[str, int]:
    buffer = []
    Block_count = 0
    Mf_size = 0

    Block = []
    for i in range(len(contents) - 0):
        byte = contents[i : i + 1].hex()
        Block.append(byte)

        if len(Block) == 16:
            buffer.append(f"Block {Block_count}: {' '.join(Block).upper()}")
            Block = []
            Block_count += 1

        if Block_count == 64:
            Mf_size = 1
        elif Block_count == 128:
            Mf_size == 2
        elif Block_count == 256:
            Mf_size = 4
    return "\n".join(buffer), Block_count, Mf_size


def get_uid(contents: bytes) -> str:
    Block = []
    for i in range(4):
        byte = contents[i : i + 1].hex()
        Block.append(byte)
    return " ".join(Block).upper()


def get_sak(contents: bytes) -> str:
    Block = []
    for i in range (5,6):
        sak = contents[i : i + 1].hex()
        Block.append(sak)
    return " ".join(Block).upper()

def get_atqa(contents: bytes) -> str:
    Block = []
    for i in range (6,8):
        atqa = contents[i : i + 1].hex()
        Block.append(atqa)
    return " ".join(Block).upper()


def assemble_code(contents: {hex}) -> str:
    conversion, Block_count, Mf_size = convert(contents)

    return f"""Filetype: Flipper NFC device
Version: 3
# Nfc device type can be UID, Mifare Ultralight, Mifare Classic, Bank card
Device type: Mifare Classic
# UID, ATQA and SAK are common for all formats
UID: {get_uid(contents)}
ATQA: 0F 01
SAK: 88
# Mifare Classic specific data
Mifare Classic type: {Mf_size}K
Data format version: 2
# Mifare Classic Blocks, '??' means unknown data
{conversion}
"""


def convert_file(input_path: str, output_path: str, base_input_path: str = None):
    input_extension = os.path.splitext(input_path)[1]
    if input_extension == ".dump":
        with open(input_path, "rb") as file:
            contents = file.read()
            
            # Get the relative path from base_input_path to maintain directory structure
            if base_input_path:
                rel_path = os.path.relpath(os.path.dirname(input_path), base_input_path)
                # If rel_path is '.', we're in the base directory
                if rel_path == '.':
                    target_dir = output_path
                else:
                    target_dir = os.path.join(output_path, rel_path)
                    os.makedirs(target_dir, exist_ok=True)
            else:
                target_dir = output_path
                
            name = os.path.split(input_path)[1]
            write_output(name.split(".dump")[0], assemble_code(contents), target_dir)



def process(path: str, output_path: str, base_input_path: str = None):
    # If base_input_path is not set, this is the first call, so set it to path
    if base_input_path is None:
        base_input_path = path if not os.path.isfile(path) else os.path.dirname(path)
    
    if os.path.isfile(path):
        convert_file(path, output_path, base_input_path)
    else:
        for filename in os.listdir(path):
            new_path = os.path.join(path, filename)

            if os.path.isfile(new_path):
                convert_file(new_path, output_path, base_input_path)
            else:
                process(new_path, output_path, base_input_path)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input-path",
        required=True,
        type=pathlib.Path,
        help="Single file or directory path to convert",
    )
    parser.add_argument(
        "-o",
        "--output-path",
        required=False,
        type=pathlib.Path,
        help="Output path, if not specified, the output .nfc file will be created in the same directory the .dump file exists within.",
    )

    args = parser.parse_args()
    return args


def main():
    args = get_args()

    if os.path.isfile(args.input_path):
        if not args.output_path:
            args.output_path = os.path.split(args.input_path)[0]
    
    os.makedirs(args.output_path, exist_ok=True)
    process(args.input_path, args.output_path)


if __name__ == "__main__":
    main()
    print("Converting...")
    time.sleep(0.3)
    print("Completed Conversion")
