#Alexis Jimenez
def menu_options(): #the display of the menu for the program
    print('\nMenu\n-------------')
    print('''1. Encode
2. Decode
3. Quit
''')

def encode(password):#function to encode password
    i = 0#start of list
    pass_string = ''
    for item in password:
        password[i] = (int(item)+3) % 10 #encodes each index by adding 3, only gives numbers from 0-9.
        pass_string += str(password[i])#adds each encoded number to an empty string
        i += 1 #increments the index for the list
    return pass_string

if __name__ == '__main__':
    program_on = True
    while program_on:#while option 3 has not been selected
        menu_options()  # calls function that shows the menu options
        option_select = int(input("\nPlease enter an option: "))
        if option_select == 1:
            password = list(input("Please enter your password to encode: "))
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")
            continue
        elif option_select == 2:#will have decode function call and other necessary statements
            pass
        elif option_select == 3:#exits program
            program_on = False
