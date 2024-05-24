"""
Author: Shep O'Keeffe
Date: 12/1
Description: A "Rock, paper, scissors"-esque program that has the user choose one of the three, answers with its own random choice, and announces who wins.
Then, it asks if the user wants to play again, starting over if the answer is yes. The entirety of the code is contained within a while loop that breaks if
the user doesn't want to play anymore or at all
Bugs: none
Challenges: while loop and delay
Sources: CS1 classes and w3schools
"""
import random #imports the random library so that it can be used in random functions
import time #imports the library containing time so that it can be used in functions of time

while True: #runs the indented code in a loop until a "break"
    user_rps = input("Rock, paper, or scissors?   ") #sets a variable equal to the user's answer to the question
    time.sleep(0.5) #adds a delay of a half second

    if user_rps == "rock": #runs the indented code as long as the variable is equal to the value
        print(random.choice(("I chose rock. It's a tie!", "I chose paper. I win!", "I chose scissors. You win!"))) #chooses a random item from the list and prints it
        time.sleep(0.5) #adds a delay of a half second
        play_again = input("Play again?   ") #sets a variable equal to the user's answer to the question
        time.sleep(0.5) #adds a delay of a half second
        if play_again == "yes": #runs the indented code as long as the variable is equal to the value
            print("loading...") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
        elif play_again == "no": #does the same as "if" but with a mutually exclusive scenario
            break #ends the "while True" loop
        else: #i.e. in any other scenario
            print("I guess you don't know how to spell.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
            print("I'm assuming that means yes.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second

    elif user_rps == "paper": #does the same as "if" but with a mutually exclusive scenario
        print(random.choice(("I chose rock. You win!", "I chose paper. It's a tie!", "I chose scissors. I win!"))) #chooses a random item from the list and prints it
        time.sleep(0.5) #adds a delay of a half second
        play_again = input("Play again?   ") #sets a variable equal to the user's answer to the question
        time.sleep(0.5) #adds a delay of a half second
        if play_again == "yes": #runs the indented code as long as the variable is equal to the value
            print("loading...") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
        elif play_again == "no": #does the same as "if" but with a mutually exclusive scenario
            break #ends the "while True" loop
        else: #i.e. in any other scenario
            print("I guess you don't know how to spell.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
            print("I'm assuming that means yes.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second

    elif user_rps == "scissors": #does the same as "if" but with a mutually exclusive scenario
        print(random.choice(("I chose rock. I win!", "I chose paper. You win!", "I chose scissors. It's a tie!"))) #chooses a random item from the list and prints it
        time.sleep(0.5) #adds a delay of a half second
        play_again = input("Play again?   ") #sets a variable equal to the user's answer to the question
        time.sleep(0.5) #adds a delay of a half second
        if play_again == "yes": #runs the indented code as long as the variable is equal to the value
            print("loading...") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
        elif play_again == "no": #does the same as "if" but with a mutually exclusive scenario
            break #ends the "while True" loop
        else: #i.e. in any other scenario
            print("I guess you don't know how to spell.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second
            print("I'm assuming that means yes.") #prints the string (the text in green)
            time.sleep(0.5) #adds a delay of a half second

    elif user_rps == "nothing": #does the same as "if" but with a mutually exclusive scenario
        print("You're no fun.") #prints the string (the text in green)
        time.sleep(0.5) #adds a delay of a half second
        break #ends the "while True" loop

    else: #i.e. in any other scenario
        print("Please answer with 'rock', 'paper', or 'scissors'.") #prints the string (the text in green)
        time.sleep(0.5) #adds a delay of a half second
        
