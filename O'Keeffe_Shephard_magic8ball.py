"""
Author: Shep O'Keeffe
Date: 11/13
Description: A "Magic 8-ball"-esque program that has the user ask a question and answers it with a random variable from a list of answers.
Runs in an infinite loop unless the user wishes to know nothing.
Bugs: none
Challenges: ehile loop and delay
Sources: CS1 classes and w3schools
"""
import time #imports the library containing time so that it can be used in functions of time
import random #imports the random library so that it can be used in random functions
while True: #runs the following code in a loop until a "break" occurs
    x = input("What do you wish to know?   ") #introduces the variable x that is equal to the user's answer to the question
    if x == "nothing": #runs the following code as long as the variable is equal to the specific value
        break #ends the loop and moves on
    time.sleep(1) #adds a delay of one second
    print(random.choice(("Uh...", "Um...", "...", "IDK.", "I'll get back to you on that one.", "Hmm...", "That's classified.", "Good question", "Wouldn't you like to know?", "Try again..."))) #chooses a random variable from the list and prints it
    time.sleep(1) #adds a delay of one second
