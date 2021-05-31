import string, random

#some global variables
password_length = 0

#boolean fields to simplify handling them later
use_uppercase = False
use_lowercase = False
use_numbers = False
use_specials = False

#define the password chars field
password_chars = ""

#define the final password result
generated_password = ""
#defined so we can reference them in our while statements
uppercase = ""
lowercase = ""
numbers = ""
specials = ""

#Get the password length from the user
while True:
	try:
		password_length = int(input("Enter the length you of the password you would like to generate (max 30): "))
		#we probably want to set a limit on how long it can be?
		if password_length <= 30:
			break

	except ValueError as error:
		print(error)
		print("Please enter an integer and try again")

#get the uppercase response
while True: # until we get a character that is either Y or N, continue
	uppercase = input("Use uppercase letters? Type Y or N: ")
		
	#if we got a Y set our value to true and leave
	if uppercase.upper() == "Y":
		use_uppercase = True
		break
	elif uppercase.upper() == "N":
		break
	print("Please enter Y or N")


#get the lowercase response
while lowercase != "Y" or lowercase != "N":
	lowercase = input("Use lowercase letters? Type Y or N: ")

	if lowercase.upper() == "Y":
		use_lowercase = True
		break
	elif lowercase.upper() == "N":
		break
	print("Please enter a Y or N")


#get the numbers response
while numbers != "Y" or numbers != "N":
	numbers = input("Do you want to use numbers? Type Y or N: ")

	if numbers.upper() == "Y":
		use_numbers = True
		break
	elif numbers.upper() == "N":
		break
	print("Please enter a Y or N")


#get the specials response
while specials != "Y" or specials != "N":
	specials = input("Do you want to use special characters? Type Y or N: ")

	if specials.upper() == "Y":
		use_specials = True
		break
	elif specials.upper() == "N":
		break
	print("Please enter a Y or N")


#for each true option, we just need to append the option to whatever the current choices are
if use_uppercase: password_chars += string.ascii_letters.upper()
if use_lowercase: password_chars += string.ascii_letters.lower()
if use_numbers: password_chars += string.digits
if use_specials: password_chars += string.punctuation

for x in range(password_length):
	generated_password += random.choice(password_chars)

#finally the results
print("Your generated password is: ", generated_password)
