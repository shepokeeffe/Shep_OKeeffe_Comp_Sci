"""
Author: Shep O'Keeffe
Date: 4/19
Description: A compilation of functions, most using inputs from the user and putting out something new
Challenges: None
Bugs: None
Sources: CS1 classes, w3schools
"""

#---IMPORTS---#

import random                                                                                 #imports the random library to be used in random functions

import time                                                                                   #imports the time library to be used in functions of time

#---DEFINITIONS---#

#first def

def verse():                                                                                  #defines a function for the code to use with the following indented code
    print("AAAAAAAAAAAAAAAAAAAAGHHHHH")                                                       #prints the string
    print("AAAAAAAGAAAAGAAAGAAAGAGAGA")                                                       #prints the string
    print("RRRRAAAAAAAAAAAAAAAAGHHHHH")                                                       #prints the string

def chorus(name):                                                                             #defines a function for the code to use with the following indented code using the variable
    print("Sorry about that", (name), "just clearing my throat")                              #prints the strings and variable
    print("Apologies if i disturbed you")                                                     #prints the string

#second def

def cool_sum(user_number_one, user_number_two):                                               #defines a function for the code to use with the following indented code using the variables
    print(user_number_one + user_number_two)                                                  #prints the result of the function contained in the parentheses

#third def

def write_list(user_list):                                                                    #defines a function for the code to use with the following indented code using the variable
    for i in user_list:                                                                       #runs the following indented code for each index in the list
        print(i)                                                                              #prints the element at that index

#fourth def

def check_list(user_item, checked_list):                                                      #defines a function for the code to use with the following indented code using the variables
    if user_item in checked_list:                                                             #runs the following indented code as long as the variable is contained in the list
        return True                                                                           #stores a true result                                                                      
    else:                                                                                     #runs the following indented code in any situation not previously accounted for
        return False                                                                          #stores a false result

#fifth def

def is_string_an_integer(string):                                                             #defines a function for the code to use with the following indented code using the variable
    if string.isnumeric():                                                                    #runs the following indented code if the string is a positive integer
        return True                                                                           #stores a true result
    else:                                                                                     #runs the following indented code in any situation not covered by the 'if' statement
        return False                                                                          #stores a false result

#sixth def

def number_in_between(low_number, high_number):                                               #defines a function for the code to use with the following indented code using the variables
    middle_number = random.randrange(low_number, high_number)                                 #creates a variable equal to a random value between those of the two other variables
    print(middle_number)                                                                      #prints the variable

#seventh def

def letter_replace(user_text, character_one, character_two):                                  #defines a function for the code to use with the following indented code using the variables
    new_text = ""                                                                             #creates an empty list
    for i in user_text:                                                                       #runs the following indented code for each index in the list
        if i == character_one:                                                                #runs the following indented code as long as the variable at that index is the specified variable
            new_text += character_two                                                         #adds the variable to the list
        else:                                                                                 #runs the following indented code in any situation not covered by the 'if' statement
            new_text += i                                                                     #adds the variable at that index to the list
    print(new_text)                                                                           #prints the variable

#---FUNCTIONS---#

#main function

def main_function():                                                                          #defines a function for the code to use with the following indented code
    
    #first func

    name = input("Hey gimme your name: ")                                                     #creates a variable equal to the user's input
    verse()                                                                                   #calls the function to be run
    verse()                                                                                   #calls the function to be run
    chorus(name)                                                                              #calls the function to be run using the variable
    verse()                                                                                   #calls the function to be run
    verse()                                                                                   #calls the function to be run
    chorus(name)                                                                              #calls the function to be run using the variable

    #second func

    while True:                                                                               #runs the following indented code in a loop until a break occurs                        
        try:                                                                                  #previews the following indented code and runs it if no errors occur                       
            user_number_one = int(input("hey gimme a number: "))                              #creates a variable equal to the user's integer input                                     
            break                                                                             #ends the while loop                       
        except ValueError:                                                                    #runs the following indented code in the exception to the 'try' function                       
            print("hey dummy try again")                                                      #prints the string

    while True:                                                                               #runs the following indented code in a loop until a break occurs                          
        try:                                                                                  #previews the following indented code and runs it if no errors occur                      
            user_number_two = int(input("hey gimme another number: "))                        #creates a variable equal to the user's integer input                                
            break                                                                             #ends the while loop                      
        except ValueError:                                                                    #runs the following indented code in the exception to the 'try' function                       
            print("hey dummy try again")                                                      #prints the string

    cool_sum(user_number_one, user_number_two)                                                #calls the function to be run using the variables

    #third func

    user_list = input("hey gimme a list of stuff separated wit' commas: ").split(',')         #creates a variable equal to the user's input that is converted into a list when its elements are split by commas

    write_list(user_list)                                                                     #calls the function to be run using the variable

    #fourth func

    checked_list = input("hey gimme another list of stuff separated wit' commas: ").split(',')#creates a variable equal to the user's input that is converted into a list when its elements are split by commas
    user_item = input("hey gimme summat from the list: ")                                     #creates a variable equal to the user's input

    print(check_list(user_item, checked_list))                                                #prints the result of the function using the variable

    #fifth func

    string = input("hey gimme a positive integer: ")                                          #creates a variable equal to the user's input

    print(is_string_an_integer(string))                                                       #prints the result of the function using the variable

    #sixth func

    while True:                                                                               #runs the following indented code in a loop until a break occurs                          
        try:                                                                                  #previews the following indented code and runs it if no errors occur                      
            low_number = int(input("hey gimme a number: "))                                   #creates a variable equal to the user's integer input                                
            break                                                                             #ends the while loop                       
        except ValueError:                                                                    #runs the following indented code in the exception to the 'try' function                       
            print("hey dummy try again")                                                      #prints the string

    while True:                                                                               #runs the following indented code in a loop until a break occurs                           
        try:                                                                                  #previews the following indented code and runs it if no errors occur                       
            high_number = int(input("hey gimme a higher number: "))                           #creates a variable equal to the user's integer input                                        
            break                                                                             #ends the while loop                      
        except ValueError:                                                                    #runs the following indented code in the exception to the 'try' function                      
            print("hey dummy try again")                                                      #prints the string

    number_in_between(low_number, high_number)                                                #calls the function to be run using the variables

    #seventh func

    user_text = input("hey gimme something: ")                                                #creates a variable equal to the user's input
    character_one = input("hey gimme a character from the thing you typed: ")                 #creates a variable equal to the user's input
    character_two = input("hey gimme another character: ")                                    #creates a variable equal to the user's input

    letter_replace(user_text, character_one, character_two)                                   #calls the function to be run using the variables
    
    time.sleep(1.5)                                                                           #adds a delay of a second and a half
    
    print("k thanks")                                                                         #prints the string

main_function()                                                                               #calls the function to be run
