"""
Author: Shep O'Keeffe
Date: 11/6
Description: A "choose your own adventure"-esque program using inputs and conditionals that has the user go through my average morning routine.
Uses while loops to refuse certain inputs and create a potentially infinite loop of the code excluding one specific input.
Bugs: If the user inputs something other than "y" or "n" after the first while loop, the code stops working.
Challenges: Multiple while loops, second-long delay
Sources: Computer science classes, https://www.w3schools.com/python/python_conditions.asp
"""

import time #imports time into the code and allows for functions using time
while True: #runs the following code in an infinite loop as long as one scenario is true or until a "break" happens
    print("You have been awakened.") #prints the string (the text in quotes)
    while True: #runs the following code in an infinite loop as long as one scenario is true or until a "break" happens
        get_up = input("Will you get out of bed?") #introduces the variable get_up that is equal to the user's answer to the question 
        time.sleep(1) #adds a delay of 1 second
        if get_up == "y": #runs the following code as long as the variable's value is equal to the string
            print("You are now out of bed.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
            took_shower = input ("Did you take a shower last night?") #introduces the variable took_shower that is equal to the user's input
            time.sleep(1) #adds a delay of 1 second
            break #stops the while loop and moves on
        elif get_up == "n": #does the same as "if" but with a mutually exclusive scenario
            print("Lazy bum.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif get_up == "Give me lasana MAOW MAOW MAOW": #does the same as "if" but with a mutually exclusive scenario 
            break #stops the while loop and moves on
        else: #accounts for any scenarios not covered by "if" or "elif" conditionals
            print("Please answer with y or n.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second

    if get_up == "Give me lasana MAOW MAOW MAOW": #runs the following code the variable's value is equal to the string
        print("The PHRASE has been uttered. Sequence aborted.") #prints the string (the text in quotes)
        break #stops the while loop and moves on

    if took_shower == "y": #runs the following code as long as the variable's value is equal to the string
        print("You are so clean already that you don't need a shower.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        take_anyway = input("Do you want to take one anyway?") #introduces the variable take_anyway that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if take_anyway == "y": #runs the following code as long as the variable's value is equal to the string
            print("You take a shower anyway, achieving a new level of cleanliness.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif take_anyway == "n": #does the same as "if" but with a mutually exclusive scenario
            print("You're plenty clean as you are.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
    elif took_shower == "n": #does the same as "if" but with a mutually exclusive scenario
        print("You are dirty.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        clean_self = input("Will you take a shower?") #introduces the variable clean_self that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if clean_self == "y": #runs the following code as long as the variable's value is equal to the string
            print("You take a shower.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif clean_self == "n": #does the same as "if" but with a mutually exclusive scenario
            print("You decide that dirty is the way to be.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
    
    brushed_teeth = input("Did you brush your teeth last night?") #introduces the variable brushed_teeth that is equal to the user's input
    time.sleep(1) #adds a delay of 1 second
    if brushed_teeth == "y": #runs the following code as long as the variable's value is equal to the string
        print("Your breath is fine, and your teeth are clean enough.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        brush_again = input("Do you want to brush them again?") #introduces the variable brush_again that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if brush_again == "y": #runs the following code as long as the variable's value is equal to the string
            print("You brush your teeth again, making your breath nice and minty.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif brush_again == "n": #does the same as "if" but with a mutually exclusive scenario
            print("Your teeth are plenty clean.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
    elif brushed_teeth == "n": #does the same as "if" but with a mutually exclusive scenario
        print("Your breath smells bad.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        brush_teeth = input("Will you brush your teeth?") #introduces the variable brush_teeth that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if brush_teeth == "y": #runs the following code as long as the variable's value is equal to the string
            print("You brush your teeth. Hooray!") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif brush_teeth == "n": #does the same as "if" but with a mutually exclusive scenario
            print("I couldn't say I haven't done it too.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
                      
    while True: #runs the code in an infinite loop as long as one scenario is true or until a "break" happens
        get_dressed = input("Will you put on some decent clothes?") #introduces the variable get_dressed that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
    
        if get_dressed == "y": #runs the following code as long as the variable's value is equal to the string
            print("Dress code. Yaaaaaaay.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
            want_food = input ("Are you hungry?") #introduces the variable want_food that is equal to the user's input
            time.sleep(1) #adds a delay of 1 second
            break #stops the while loop and moves on
        elif get_dressed == "n": #does the same as "if" but with a mutually exclusive scenario
            print("I'm afraid I can't let you do that.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second

    if want_food == "y": #runs the following code as long as the variable's value is equal to the string
        print("Want. Food.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        eat_food = input("Will you go and eat some breakfast?") #introduces the variable eat_food that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if eat_food == "y": #runs the following code as long as the variable's value is equal to the string
            print("Yum yum.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif eat_food == "n": #does the same as "if" but with a mutually exclusive scenario
            print("Who are you, Ghandi?") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
    elif want_food == "n": #does the same as "if" but with a mutually exclusive scenario
        print("You have no rumble in your tummy.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        eat_anyway = input("Do you want to eat anyway?") #introduces the variable eat_anyway that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if eat_anyway == "y": #runs the following code as long as the variable's value is equal to the string
            print("Breakfast is the most important meal of the day.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif eat_anyway == "n": #does the same as "if" but with a mutually exclusive scenario
            print("You're more of a lunch person, I guess.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second

    dumb_loop = 0 #introduces the variable dumb_loop and sets its value to zero
    while dumb_loop <8: #runs the code in an infinite loop as long as the value of dumb_loop is less than eight
        print("Driving...") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        dumb_loop+=1 #adds 1 to the value of dumb_loop
    
    print("School!") #prints the string (the text in quotes)
    time.sleep(1) #adds a delay of 1 second

    did_work = input("Did you do your homework last night?") #introduces the variable did_work that is equal to the user's input
    time.sleep(1) #adds a delay of 1 second
    if did_work == "y": #runs the following code as long as the variable's value is equal to the string
        print("How responsible of you.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        do_more = input("do you want to get ahead of your next assignments?") #introduces the variable do_more that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if do_more == "y": #runs the following code as long as the variable's value is equal to the string
            print("You do MORE work. Nerd.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif do_more == "n": #does the same as "if" but with a mutually exclusive scenario
            print("You go to the dining hall and get a lemonade.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
    elif did_work == "n": #does the same as "if" but with a mutually exclusive scenario
        print("I don't blame you. You were busy doing nothing.") #prints the string (the text in quotes)
        time.sleep(1) #adds a delay of 1 second
        do_work = input("Do you fear the wrath of your teachers?") #introduces the variable do_work that is equal to the user's input
        time.sleep(1) #adds a delay of 1 second
        if do_work == "y": #runs the following code as long as the variable's value is equal to the string
            print("You get your work done with little time to spare.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second
        elif do_work == "n": #does the same as "if" but with a mutually exclusive scenario
            print("0/100.") #prints the string (the text in quotes)
            time.sleep(1) #adds a delay of 1 second

    print("Time for computer science.") #prints the string (the text in quotes)
    time.sleep(1) #adds a delay of 1 second
    print("You open your computer.") #prints the string (the text in quotes)
    time.sleep(1) #adds a delay of 1 second
    print("You start your program.") #prints the string (the text in quotes)
    time.sleep(1) #adds a delay of 1 second
    print("A message pops up:") #prints the string (the text in quotes)
    time.sleep(1) #adds a delay of 1 second
