# Disclaimer

SkylanderConverter is based off of equipters work. I encourage you to check out his github that I forked this from.

# SkylanderConverter
Skylander Converter is a python script that converts Skylanders .BIN files to [FlipperZero's](https://flipperzero.one/) custom .nfc format. 

PLEASE NOTE .BIN files are the same as .SKY and .DUMP files. Make sure you rename them to .BIN for this to work.

Worth noting, SkylanderConverter also handles all of the below for the file header:
- UID
- SAK
- ATQA
- Storage Size 

**Works for 4-Byte UIDs just make sure youre using the correct script when converting :)**
  

## Acknowledgements
| [Github](https://github.com/equipter) | [Twitter](https://twitter.com/Equip0x80) | [Reddit](https://www.reddit.com/user/equipter) | equip paypal: equipter@outlook.com | [Discord](https://discord.gg/e9XzfG5nV5) |
| :---: | :---: | :---: | :---: | :---: |

 [Lucaslhm's Amiibo converter script for MFUL](https://github.com/Lucaslhm/AmiiboFlipperConverter) for code inspo

## Download and Usage
### **Requires Python 3**

1. Download code Either through `git clone` or by simply pressing the green [Code] Button at the top and downloading the zip. 
2. Place your (.bin) Binary files in the "assets" folder or create your own folder(s) and place the files in there. 
3. Imaginators.py is the correct script for Skylanders Imaginators figures.
4. Regulars.py is the correct script for all other Skylanders figures.

The Parameters for SkylanderConverter are as such 

`-i / --input-path` - mandatory file input location, link to file in directory or whole directory to be converted. 

`-o / --output-path` - optional file output location, if no output path is specified, the generated nfc file will be created in the same directory as the input binary file. 

### Example
This is an example of what to type in the terminal

`python3 4B_Converter.py -i assets/example.bin`
after running you should be met with "Completed Conversion" and a new file appearing in your assets folder with the same name as your binary file but with a .nfc extension and file format. 

![image](https://user-images.githubusercontent.com/72751518/182514125-be1aedb1-59e9-4994-906a-df83f36c0f66.png)

![image](https://user-images.githubusercontent.com/72751518/182514195-c766ca6a-234f-43e9-a779-fce67894f5e6.png)




## Support

As of writing this, this will ONLY work with Skylanders Imaginators Figures/Level Packs. I don't have figures from the other game yet. When I get them, I'll make changes to the script here :)

For support, Message froyop12 on discord froyop12#8300

This has only been tested on Nintendo Switch. While it should work on other systems, it's not guaranteed.



