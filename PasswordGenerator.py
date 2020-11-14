import string as st
import sys
import random

upperCase = st.ascii_uppercase
lowerCase = st.ascii_lowercase
digits = st.digits
specialChars = st.punctuation

passwordLength = 0
while passwordLength < 8:
    try :
        info = input("Enter website or email address: ")
        passwordLength = int(input("Enter password length, minimum 8 letters, enter 0 to quit: "))
        if passwordLength == 0:
            print("See you next time.")
            sys.exit(0)
    except ValueError: 
        print("Please enter a number!")

concatString = upperCase + lowerCase + digits + specialChars
characters = list(concatString)

generatedPassword = "".join(random.sample(characters, passwordLength))
print("Generating password...")
print("Your password is: " + generatedPassword)

file = open("accounts.txt", "a")
file.write(info + ": " + generatedPassword + "\n")
file.close()
print("Exiting... Goodbye!") 