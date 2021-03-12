#!/bin/python3
# Manipulates the text saved to the clipboard, or from std in. If not text provided, uses clipboard. By default, will do spongegar formatting (lIkE tHiS)
import argparse
import pyperclip
import logging

#logging
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s--%(levelname)s:  %(message)s")

##Logging toggle
logging.disable()
##
parser = argparse.ArgumentParser(description="Manipulates text from std in. If no text is provided, uses stdin.")
parser.add_argument('--text','-t',type=str,help="the text to manipulate if not provided by std.in")
parser.add_argument('--clipboard','-c',help="copy output to clipboard",action="store_true")
parser.add_argument('--surround','-s',help="text to surround input. enter only the left side- and it will be mirrored on the right")

# Format flags- mutually exclusive
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--spongegar","-sp", help="Formats in sPoNgEgAr", action='store_true')
group.add_argument("--leet","-l",help="Formats in 1337",action='store_true')
args = parser.parse_args()

# text or clipboard
input_text = ""
if args.text:
    input_text = args.text
else:
    input_text = pyperclip.paste()

# verbose messenger
def verbose_message(message):
    if args.verbose:
        print(message)
    else:
        pass

# clip flag function
def process_clipboard_flag(string):
    if args.clipboard:
        pyperclip.copy(string)
        return string
    else:
        return string
#spongegar
def spongegar_formatter(string):
    string = string.lower()
    return_string = ""
    letter_count = 1
    for letter in string:
        logging.debug(f'Current letter:{letter} | letter count: {letter_count}')
        if letter_count % 2 == 0:
            return_string += letter.upper() 
        else:
            return_string += letter
        letter_count += 1
    process_clipboard_flag(return_string)
    return return_string
#1337
def leet_formatter(string):
    string = string.upper()

    leet_dict = {
        "A":"4",
        "B":"8",
        "C": "¢",
        "D": "d",
        "E": "3",
        "F": "ƒ",
        "G": "6",
        "H":"h",
        "I":"1",
        "J":"j",
        "K":"|<",
        "L":"1",
        "M":"m",
        "N":"n",
        "O": "Ø",
        "P": "p",
        "Q":"q",
        "R":"r",
        "S":"5",
        "T":"7",
        "U":"u",
        "V":r"\/",
        "W":"w",
        "X":"x",
        "Y":"¥",
        "Z":"2",
    }

    def leet_returner(letter):
        if letter not in leet_dict:
            return letter
        else:
            return leet_dict[letter]

    return_string=""
    letter_count = 1
    
    for letter in string:
        logging.debug(f'Current letter:{letter} | letter count: {letter_count}')
        return_string += leet_returner(letter)

    return return_string


# surround
def surround_formatter(string,string_to_surround):
    if args.surround:
        left = string +" "
        right = " "
        for char in range(len(string)-1,-1,-1):
            right+=string[char]
        return left + string_to_surround + right
    else:
        return string_to_surround

# switch/output
if args.spongegar:
    print(process_clipboard_flag(surround_formatter(args.surround, spongegar_formatter(input_text))))
elif args.leet:
    print(process_clipboard_flag(surround_formatter(args.surround,leet_formatter(input_text))))
else:
    raise FormatError('No Format Argument Given. Use -h for help') 
