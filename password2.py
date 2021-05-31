import string, random

#create some global variables
password_length = 0

#define the password chars field
password_chars = ""

#define the final password result
generated_password = ""

def get_password_length():
	pass_length = ""
	#Get the password length from the user
	while True:
		try:
			pass_length = int(input("Enter the length you of the password you would like to generate (max 30): "))
			#we probably want to set a limit on how long it can be?
			if pass_length <= 30:
				break

		except ValueError as error:
			print(error)
			print("Please enter an integer and try again")

	return pass_length


#we can use a method to encapsulate everything we need to do to get the user inputs.
def get_password_options():

	#define these before hand so we can reference them in our while statements
	upperChars = string.ascii_letters.upper()
	lowerChars= string.ascii_letters.lower()
	numberChars = string.digits
	specialChars = string.punctuation
	#our return value
	pass_chars = ""

	#get the uppercase response
	while uppercase != "Y" or uppercase != "N": # until we get a character that is either Y or N, continue
		uppercase = input("Use uppercase letters? Type Y or N: ")
		
		#if we got a Y set our value to true and leave
		if uppercase == "Y":
			pass_chars += upperChars
		elif uppercase=="N":
                    break

		#we did not get a valid response go back to start
		print("Please enter Y or N")


	#get the lowercase response
	while lowercase != "Y" or lowercase != "N":
		lowercase = input("Use lowercase letters? Type Y or N: ")

		if lowercase== "Y":
			pass_chars += lowerChars
		elif lowercase== "N":
			break

		print("Please enter a Y or N")


	#get the numbers response
	while numbers != "Y" or numbers != "N":
		numbers = input("Do you want to use numbers? Type Y or N: ")

		if numbers == "Y":
			pass_chars += numberChars
		elif numbers == "N":
			break

		print("Please enter a Y or N")


	#get the specials response
	while specials != "Y" or specials != "N":
		specials = input("Do you want to use special characters? Type Y or N: ")

		if specials == "Y":
			pass_chars += specialChars
		elif specials == "N":
			break

		print("Please enter a Y or N")

	return pass_chars 


#the final method to perform the actual password
def generate_password(pass_length, pass_chars):
	gen_password = ""
	x = 0
	#not sure why we would do this 
	#for x in range(length):
	#and not this, i think its simpler but you choose
	while x < password_length:
		gen_password += random.choice(pass_chars)
		x += 1
		
	return gen_password


#this is the code that will run when you execute this python script
#we do not have to do anything but call the methods in order


#call the first method that gets our desired length
password_length = get_password_length()

#next call the method to get the type options and return our optional characters
password_chars = get_password_options()

#now, call the last method that will generate our password and return it, we need to send these two values to it
generated_password = generate_password(password_length, password_chars)

#finally, display the results
print("Your generated password is: ", generated_password)

