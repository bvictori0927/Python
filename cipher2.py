
import string    # Import the string library to generate our character list


# Prompt the user for a plain text string to be encrypted.
message = input("Enter the message to be encrypted here: ")


# Prompt the user for a key size. Verify that is is a int type.
while True:
    try:
        key = int(input("Please enter your key size: "))
        break
    except ValueError as error:
        print(error)
        print("Please enter an integer for the key and try again.")

# Set the mode to either encrypt or decrypt
mode = input("Please enter E for encrypt and D for decrypt: ")

# Create Character Base 
SYMBOLS = string.ascii_letters + string.digits + string.punctuation + " "

# To store our translated message
translated = ''

for symbol in message:    
    if symbol in SYMBOLS: 
        symbolIndex = SYMBOLS.find(symbol)  

        # The shift
        if mode in ['encrypt', 'ENCRYPT', 'e', 'E']:
            translatedIndex = symbolIndex + key
        elif mode in ['decrypt', 'DECRYPT', 'd', 'D']:
            translatedIndex = symbolIndex - key

            # What do I do when it wraps around? There's a script for that!
        if translatedIndex >= len(SYMBOLS):
            translatedIndex -= len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex += len(SYMBOLS)

        
        translated += SYMBOLS[translatedIndex]
    else:
        
        translated += symbol


print(translated)
