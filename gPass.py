# gPass
# Generator: Passwords
# by Cyphrags

# Imports
import os
import random

from optparse import OptionParser

# Variables
import sys

lettersLowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettersUppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ["!", "\"", "$", "%", "&", "/", "(", ")", "=", "?", "{", "[", "]", "}", "\\", "@", "€", "+", "*", "~", "#", "'", ",", ";", ".", ":", "-", "_"]
specialCharactersAdvanced = ["^", "°", "§", "`", "´", "<", ">", "|"]

# Functions

def generatePassword(length, whitelist, blacklist):
    password = internalGeneratePassword(length, whitelist)
    while internalContainsBlacklist(password, blacklist):
        password = internalGeneratePassword(length, whitelist)
    return password

def internalGeneratePassword(length, whitelist):
    password = ""
    for x in range(length):
        password += random.choice(whitelist)
    return password

def internalContainsBlacklist(password, blacklist):
    for char in blacklist:
        if char in password:
            return True
    return False

# Program

### Setup OptionParser and check given options
parser = OptionParser()
parser.add_option("-o", "--output", dest="flagOutput", help="File to output passwords to in the format of \"Password1\\r\\nPassword2\\r\\n\"")
parser.add_option("-w", "--whitelist", dest="flagWhitelist", help="List or file containing characters/words to be used for the password generation. The characters/words need to be separated by \\r\\n")
parser.add_option("-b", "--blacklist", dest="flagBlacklist", help="List of file containing characters/words which shouldn't be used for password generation. The characters/words need to be separated by \\r\\n")

parser.add_option("-a", "--amount", dest="flagAmount", help="Amount of passwords to generate")
parser.add_option("-l", "--length", dest="flagLength", help="Lengths for the passwords")

parser.add_option("--llc", dest="flagLLC", help="Use lowercase letters")
parser.add_option("--luc", dest="flagLUC", help="Use uppercase letters")
parser.add_option("--num", dest="flagNumbers", help="Use numbers")
parser.add_option("--sc", dest="flagSC", help="Use special characters")
parser.add_option("--sca", dest="flagSCA", help="Use additional (generally not accepted) special characters")

(options, args) = parser.parse_args()

flagOutput = None if options.flagOutput is None else str(options.flagOutput)
flagWhitelist = None if options.flagWhitelist is None else str(options.flagWhitelist)
flagBlacklist = None if options.flagBlacklist is None else str(options.flagBlacklist)

flagAmount = 1 if options.flagAmount is None or not str(options.flagAmount).isdigit() else int(options.flagAmount)
flagLength = 8 if options.flagLength is None or not str(options.flagLength).isdigit() else int(options.flagLength)

flagLLC = True if options.flagLLC is None else str(options.flagLLC).lower() == "true"
flagLUC = True if options.flagLUC is None else str(options.flagLUC).lower() == "true"
flagNumbers = True if options.flagNumbers is None else str(options.flagNumbers).lower() == "true"
flagSC = True if options.flagSC is None else str(options.flagSC).lower() == "true"
flagSCA = False if options.flagSCA is None else str(options.flagSCA).lower() == "true"

### Generate the list of usable characters

whitelist = []
blacklist = []

if flagWhitelist is not None:
    if os.path.isfile(flagWhitelist):
        with open(flagWhitelist) as f:
            content = f.read()
            for line in content.split("\r\n"):
                whitelist.append(line)
    else:
        for char in flagWhitelist.split("\r\n"):
            whitelist.append(char)

if flagBlacklist is not None:
    if os.path.isfile(flagBlacklist):
        with open(flagBlacklist) as f:
            content = f.read()
            for line in content.split("\r\n"):
                blacklist.append(line)
    else:
        for char in flagBlacklist.split("\r\n"):
            blacklist.append(char)

if flagLLC:
    for x in range(len(lettersLowercase)):
        whitelist.append(lettersLowercase[x])

if flagLUC:
    for x in range(len(lettersUppercase)):
        whitelist.append(lettersUppercase[x])

if flagNumbers:
    for x in range(len(numbers)):
        whitelist.append(numbers[x])

if flagSC:
    for x in range(len(specialCharacters)):
        whitelist.append(specialCharacters[x])

if flagSCA:
    for x in range(len(specialCharactersAdvanced)):
        whitelist.append(specialCharactersAdvanced[x])


### Remove duplicates from lists
whitelist = list(set(whitelist))
blacklist = list(set(blacklist))

if len(whitelist) == 0:
    print("[!] Error: No characters selected for password generation!")
    sys.exit(1)

### Generate the passwords
passwords = []

for x in range(flagAmount):
    passwords.append("")

for x in range(flagAmount):
    passwords[x] = generatePassword(flagLength, whitelist, blacklist)
    print("[#] Password %s: %s" % (x + 1, passwords[x]))

### Output to file
if flagOutput is not None:
    flagOutput = os.path.expandvars(flagOutput)
    open(flagOutput, "w+")
    if os.path.isfile(flagOutput):
        with open(flagOutput, 'w') as f:
            for x in range(len(passwords)):
                f.writelines(passwords[x] + "\n")
    else:
        print("[!] '%s' does not seem to be a file!" % flagOutput)

