''' 
Caesar Cipher program
CaesarCipher.py
BMeadows
Used to encry/decrypt data
'''

#Bringing in the String library to generate character base 
import string


#Prompt the user 
message= input("Enter the message or phrase to be encrypted or decrypted: ")
#Get the key from the user 
while True:
    try:
        key = int(input('Please enter your key size: '))
        break
    except ValueError as error: 
        print(error)
        print('Please enter an integer for the key and try again.')
#getting the mode setting
mode=input('Please enter E for encrypt and D for decrypt!')
#Create my character base 
SYMBOLS= string.ascii_letters + string.punctuation + string.digits + " "
#to store translated message

translated= ''
#Code to encrypt/decrypt
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

## The shift 
        if mode in['e','E','ENCRYPT','encrypt']:
                translatedIndex = symbolIndex + key
        elif mode in ['DECRYPT','decrypt','D','d']:
                translatedIndex = symbolIndex - key
       
#What do I do when it wraps around? There's a script for that!
        if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
        elif translatedIndex <= 0:
                translatedIndex += [len(SYMBOLS)]

                translated += SYMBOLS[translatedIndex]
    else:
                translated += symbol
print(translated)

