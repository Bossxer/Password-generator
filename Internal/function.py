import string
import secrets
from colorama import init, Fore, Style
import ctypes
import os
import pyperclip
import sys
import time

def setup():
    init() # Initialize colorama module for colors
    ctypes.windll.kernel32.SetConsoleTitleW("Password Generator") # changes console title
    print(Fore.CYAN + "██████╗░░█████╗░░██████╗░██████╗  ░██████╗░███████╗███╗░░██╗██╗" + Style.RESET_ALL) # part 1 of the big text
    print(Fore.CYAN + "██╔══██╗██╔══██╗██╔════╝██╔════╝  ██╔════╝░██╔════╝████╗░██║██║" + Style.RESET_ALL) # part 2 of the big text
    print(Fore.CYAN + "██████╔╝███████║╚█████╗░╚█████╗░  ██║░░██╗░█████╗░░██╔██╗██║██║" + Style.RESET_ALL) # part 3 of the big text
    print(Fore.CYAN + "██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗  ██║░░╚██╗██╔══╝░░██║╚████║╚═╝" + Style.RESET_ALL) # part 4 of the big text
    print(Fore.CYAN + "██║░░░░░██║░░██║██████╔╝██████╔╝  ╚██████╔╝███████╗██║░╚███║██╗" + Style.RESET_ALL) # part 5 of the big text
    print(Fore.CYAN + "╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝" + Style.RESET_ALL) # part 6 of the big text

def append_to_file(file_name, data): # defines function to append data to a file
    with open(file_name + ".txt", 'a') as file: # opens file in append mode
        file.write(data + '\n') # writes data to file

def password_gen(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    if length < 12: 
        raise ValueError("Password length should be at least 12 characters.") # checks if the length is less than 12 and if it is it raises an error

    options = ''
    if include_uppercase:
        options += string.ascii_uppercase # adds the uppercase alphabet to the options variable 
    if include_lowercase:
        options += string.ascii_lowercase # adds the lowercase alphabet to the options variable
    if include_numbers:
        options += string.digits # adds the digits to the options variable
    if include_symbols:
        options += string.punctuation # adds the symbols to the options variable

    if not options:
        raise ValueError("At least one character type should be selected.") # needs one option to be selected otherwise it raises an error

    password = []
    if include_uppercase:
        password.append(secrets.choice(string.ascii_uppercase)) # adds a random uppercase alphabet letter from the selected options to the password list
    if include_lowercase:
        password.append(secrets.choice(string.ascii_lowercase)) # adds a random lowercase alphabet letter from the selected options to the password list 
    if include_numbers:
        password.append(secrets.choice(string.digits)) # adds a random digits from the selected options to the password list
    if include_symbols:
        password.append(secrets.choice(string.punctuation)) # adds a random symbol from the selected options to the password list

    remaining_length = length - len(password)
    password.extend(secrets.choice(options) for _ in range(remaining_length)) # adds random characters from the selected options to the password list

    secrets.SystemRandom().shuffle(password) # shuffles the password list so its truly random

    return ''.join(password) # returns the password list as a string

def get_number_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.") # makes the user enter a valid number so its not a string and errors out

def generate_1_password():
    os.system('cls')
    length = get_number_input(Fore.BLUE + "Enter the length of the password(min 12): " + Style.RESET_ALL) # gets the length of the password from an input and stores it in the length variable
    include_uppercase = input(Fore.BLUE + "Include uppercase characters? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use uppercase in there password
    include_lowercase = input(Fore.BLUE + "Include lowercase characters? (y/n): " + Style.RESET_ALL).lower() == 'y' # also gets if the user wants to use lowercase in there password
    include_numbers = input(Fore.BLUE + "Include numbers? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use numbers in there password
    include_symbols = input(Fore.BLUE + "Include symbols? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use symbols in there password

    password = password_gen(length, include_uppercase, include_lowercase, include_numbers, include_symbols) # generates the password using the password_gen function
    print(Fore.GREEN + "Generated password: " + Style.RESET_ALL + password) # prints the generated password

    save = input(Fore.BLUE + "Do you want to save the password to a file or copy it to clipboard? (file/copy): " + Style.RESET_ALL).lower() # ask if the user wants to save it or copy it
    if save.lower() == 'file': # if the user wants to save it to a file
        file_name = input(Fore.BLUE + "Enter the file name: " + Style.RESET_ALL)
        append_to_file(file_name, password)
        print(Fore.GREEN + "Password saved to file." + Style.RESET_ALL) # gets and input of a file name from a user than appends it and prints that is succfully saved to a file
    elif save.lower() == 'copy':
        pyperclip.copy(password)
        print(Fore.GREEN + "Password copied to clipboard." + Style.RESET_ALL) # copys the password to the users clipboard
    time.sleep(2)
    Main() # goes back to the main function

def generate_multiple_passwords():
    os.system('cls')
    count = get_number_input(Fore.BLUE + "Enter the number of passwords to generate: " + Style.RESET_ALL) # gets the number of passwords to generate from the user
    length = get_number_input(Fore.BLUE + "Enter the length of the password(min 12): " + Style.RESET_ALL) # gets the length of the password from the user
    include_uppercase = input(Fore.BLUE + "Include uppercase characters? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use uppercase in there password
    include_lowercase = input(Fore.BLUE + "Include lowercase characters? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use lowercase in there password
    include_numbers = input(Fore.BLUE + "Include numbers? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use numbers in there password
    include_symbols = input(Fore.BLUE + "Include symbols? (y/n): " + Style.RESET_ALL).lower() == 'y' # gets if the user wants to use symbols in there password

    passwords = [password_gen(length, include_uppercase, include_lowercase, include_numbers, include_symbols) for _ in range(count)] # generates the passwords using the password_gen function
    print(Fore.GREEN + "Generated passwords: " + Style.RESET_ALL)
    for password in passwords:
        print(password) # prints the generated passwords

    save = input(Fore.BLUE + "Do you want to save the passwords to a file? (y/n): " + Style.RESET_ALL).lower() # asks if the user wants to save the passwords to a file
    if save.lower() == 'y':
        file_name = input(Fore.BLUE + "Enter the file name: " + Style.RESET_ALL)
        for password in passwords:
            append_to_file(file_name, password)
        print(Fore.GREEN + "Passwords saved to file." + Style.RESET_ALL) # if the user wants to save the passwords to a file it gets a file name from the user and appends the passwords to the file
    time.sleep(2)
    Main() # goes back to the main function

def Main():
    os.system('cls')
    setup()
    print(Fore.GREEN + "Select an option: " + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Generate password" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Mutiple Password Generator" + Style.RESET_ALL)
    print(Fore.RED + "3. Exit" + Style.RESET_ALL)
    Choice = get_number_input(Fore.BLUE + "Enter your choice: " + Style.RESET_ALL) # has 3 choices on what they want to do and there input is stored in the choice variable

    if Choice == 1:
        try:
            generate_1_password()
        except ValueError as e:
            print(Fore.RED + "Error:", e)
            time.sleep(2)
            Main() # if the user selects 1 it goes to the generate_1_password function and if there is an error it prints the error and goes back to the main function
    elif Choice == 2:
        try:
            generate_multiple_passwords()
        except ValueError as e:
            print(Fore.RED + "Error:", e)
            time.sleep(2)
            Main() # if the user selects 2 it goes to the generate_multiple_passwords function and if there is an error it prints the error and goes back to the main function
    elif Choice == 3:
        print("Exiting program...")
        sys.exit() # if the user selects 3 it prints that it is exiting the program and exits the program
    else:
        print("Invalid choice. Please select a valid option.") # if the user selects an invalid option it prints that it is invalid and goes back to the main function