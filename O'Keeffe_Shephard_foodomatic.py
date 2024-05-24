'''
Author: Shep O'Keeffe
Date: 3/29
Description: A random insult generator that plugs random words from three lists into a template sentence for an
amount of times specified by a user input.
Challenges: Three lists, no value errors
Bugs: None
Sources: w3schools, Ms. Marciano
'''
import random                                                                                                    #imports the random library to be used for random functions

features = ["a brain", "eyes", "a nose", "ears", "a mouth", "arms", "legs", "hands", "feet", "hair",]            #Creates a list of features
descriptors = ["dumb", "smelly", "boring", "weird", "gross", "hideous", "disgusting", "dirty", "slimy", "nasty"] #Creates a list of descriptors
insults = ["pig", "dog", "slug", "mule", "fish", "worm", "bug", "cow", "rat", "snake"]                           #Creates a list of insults

while True:                                                                                                      #Runs the following indented code until a 'break' occurs    
    try:                                                                                                         #Previews the following indented code; runs it unless an exception occurs
        numero = int(input("Pick a number: "))                                                                   #Creates a variable equal to the user's input
        break                                                                                                    #Ends the 'while True' loop; moves on
    except ValueError:                                                                                           #Runs the following code if the input's value causes an error
        print('Dummy. Try again.')                                                                               #Prints the string

for i in range(numero):                                                                                          #Runs the following indented code for the amount specified by the input
        response = input("Hey you! ")                                                                            #Creates a variable equal to the user's input
        if response == "lalala not listening":                                                                   #Runs the following indented code in this situation
            break                                                                                                #Ends the 'while True' loop
        else:                                                                                                    #Runs the following indented code in any other situation
            print(f'''
            You've got {random.choice(features)}
            like a {random.choice(descriptors)} {random.choice(insults)}.
            ''')                                                                                                 #Prints the strings (including random elements chosen from the given lists)
