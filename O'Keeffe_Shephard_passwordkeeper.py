'''
Author: Shep O'Keeffe
Date: 5/13
Description: a "password keeper" that prompts the user for websites and their log-in info.
It allows the user to access their info for all websites or just one, change their info for
a website, or end the program. 
Challenges: retroactive addition of information, changing of information
Bugs: none
Sources: CS1 classes
'''

websites = []                                                                                #creates an empty list
usernames = []                                                                               #creates an empty list
passwords = []                                                                               #creates an empty list

def add_info():                                                                              #defines a function to be used later in the code
    '''
    adds the user's info to the lists
    args:
        enter_website, enter_username, enter_password (strings)
    '''
    websites.append(enter_website)                                                           #adds the variable to the end of the list
    usernames.append(enter_username)                                                         #adds the variable to the end of the list
    passwords.append(enter_password)                                                         #adds the variable to the end of the list

def give_all():                                                                              #defines a function to be used later in the code
    '''
    prints each website and its respective information
    args:
        websites, usernames, passwords (lists)
    returns:
        string: all information
    '''
    for i in range(len(websites)):                                                           #runs the indented code for each index in the list
        print(websites[i], usernames[i], passwords[i])                                       #prints the item in each list at the specified index
        
def give_specific():                                                                         #defines a function to be used later in the code
    '''
    finds a specific website and prints its information
    args:
        websites, usernames, passwords (lists)
        specific_choice (string)
    returns:
        string: website's information
        string: not found message
    '''
    for i in range(len(websites)):                                                           #runs the indented code for each index in the list
        if websites[i] == specific_choice:                                                   #runs the indented code if the variable is at the index in the list
            print(f'''
{usernames[i]}
{passwords[i]}
''')                                                                                         #prints the item at the index in each list in one string
    if specific_choice not in websites:                                                      #runs the indented code if the variable is not contained in the list
        print('''
website not found''')                                                                        #prints the string

def change_info():                                                                           #defines a function to be used later in the code
    '''
    allows the user to change the information for a website
    args:
        websites, usernames, passwords (lists)
        target_choice, new_username, new_password (strings)
    returns:
        string: not found message
    '''
    for i in range(len(websites)):                                                           #runs the indented code for each index in the list
        if websites[i] == target_choice:                                                     #runs the indented code if the variable is at the index in the list
            websites.pop(i)                                                                  #removes the item at the index in the list
            usernames.pop(i)                                                                 #removes the item at the index in the list
            passwords.pop(i)                                                                 #removes the item at the index in the list
            websites.append(target_choice)                                                   #adds the variable to the end of the list
            usernames.append(new_username)                                                   #adds the variable to the end of the list
            passwords.append(new_password)                                                   #adds the variable to the end of the list
    if target_choice not in websites:                                                        #runs the indented code if the variable is not contained in the list
        print('''
website not found''')                                                                        #prints the string

while True:                                                                                  #runs the indented code in a loop until a 'break' happens
    while True:                                                                              #runs the indented code in a loop until a 'break' happens
        try:                                                                                 #runs the indented code unless an error occurs
            function_choice = int(input("""
        Would you like to:
        1. enter log-in information for a website?
        2. see the information for all of your websites?
        3. see the information for one specific website?
        4. change the information for a website?
        or 5. end the program?

        """))                                                                                        #creates an integer variable equal to the user's answer to the string
            break                                                                            #ends the 'while True' loop
        except ValueError:                                                                   #runs the indented code in an exception to the 'try' function (a value error)
            print("Try again")                                                               #prints the string
                                                                                                    
    if function_choice == 1:                                                                 #runs the indented code if the variable is equal to a specific value
        enter_website = input("Enter a website to create a sign-in for: ")                   #creates a variable equal to the user's answer to the string
        enter_username = input("Enter your username for that website: ")                     #creates a variable equal to the user's answer to the string
        enter_password = input("Enter your password for that account: ")                     #creates a variable equal to the user's answer to the string
        add_info()                                                                           #calls the function to be run

    elif function_choice == 2:                                                               #runs the indented code if the variable is equal to a mutually exclusive value
        give_all()                                                                           #calls the function to be run

    elif function_choice == 3:                                                               #runs the indented code if the variable is equal to another specific value
        specific_choice = input("Which website would you like to see the information for? ") #creates a variable equal to the user's answer to the string
        give_specific()                                                                      #calls the function to be run

    elif function_choice == 4:                                                               #runs the indented code if the variable is equal to another specific value
        target_choice = input("Which website would you like to change the information for? ")#creates a variable equal to the user's answer to the string
        new_username = input("What would you like the username to be changed to? ")          #creates a variable equal to the user's answer to the string
        new_password = input("What would you like the password to be changed to? ")          #creates a variable equal to the user's answer to the string
        change_info()                                                                        #calls the function to be run

    elif function_choice == 5:                                                               #runs the indented code if the variable is equal to another specific value
        print("Terminating program...")                                                      #prints the string
        break                                                                                #ends the 'while True' loop

    else:                                                                                    #runs the indented code in any situation not covered by the prior 'if's and 'elif's
        print("What?")                                                                       #prints the string

