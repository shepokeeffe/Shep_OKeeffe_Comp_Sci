"""
Author: Shep O'Keeffe
Date: 11/31/24
Description: Tic-tac-toe. The user can play a bot or another user (on the same device) as many times as they want.
Bugs: stops working if fewer than 2 names are entered in 2 player mode
Sources: CS classes
"""
import random
import time

def check_choice(letter):
    '''
    gets where the player wants to put their letter and checks if their choice is available 
    args:
        letter (str) - the current player's letter
    returns:
        player_choice (int) - the location on the board where the player wants to put their letter
    '''
    while True:
        try:
            player_choice = int(input(f"Where would you like to put your {letter}? "))
            for i in board:
                if player_choice in i:
                    return player_choice
        except ValueError:
            print("Enter a number.")
        print("That's not an available spot.")

def check_bot_choice():
    '''
    chooses a random available location on the board in which the bot's letter can be placed
    returns:
        bot_choice (int) - the location on the board where the bot's letter will go
    '''
    while True:
        bot_choice = random.randint(0,9)
        for i in board:
            if bot_choice in i:
                print('')
                return bot_choice

def place_letter(letter, player_choice):
    '''
    finds the player's chosen location on the board and puts their letter there
    args:
        letter (str) - the current player's letter
        player_choice (int) - the location on the board where the player wants to put their letter 
    returns:
        str - the board with the player's letter in their location of choice
    '''
    for row in range(3):
        for column in range(3):
            if board[row][column] == player_choice:
                board[row][column] = letter
    for i in board:
        print(i)

def check_win(letter):
    '''
    checks all possible win conditions to see if the player has won the game
    args:
        letter (str) - the current player's letter
    returns:
        "win" (str) - indication that the player has won
    '''
    for i in range(0,3):
        if board[i][0] == letter and board[i][1] == letter and board[i][2] == letter:
            return("win")
        elif board[0][i] == letter and board[1][i] == letter and board[2][i] == letter:
            return("win")
    if board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return("win")
    elif board[2][0] == letter and board[1][1] == letter and board[0][2] == letter:
        return("win")

while True:
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]    
    play = input("Would you like to play Tic Tac Toe? ")
    
    if play == "yes":
        while True:
            players = input("1 or 2 players? ")
            
            if players == "1":
                #Player playing against bot
                while True:
                    letter = input("Would you like to play as X or O? ")
                                        
                    if letter == "x":
                        #Player as X and bot as O
                        for i in board:
                            print(i)
                        #Plays the game with a max of 9 plays (for 9 spots on the board), ending when someone wins
                        for i in range(0, 4):
                            x_choice = check_choice("X")
                            place_letter("X", x_choice)
                            if check_win("X") == "win":
                                print("You win!")
                                break
                            time.sleep(1) #waits a second before continuing
                            o_choice = check_bot_choice()
                            place_letter("O", o_choice)
                            if check_win("O") == "win":
                                print("You lose!")
                                break
                        if check_win("O") != "win" and check_win("X") != "win":
                            x_choice = check_choice("X")
                            place_letter("X", x_choice)
                            if check_win("X") == "win":
                                print("You win!")
                            else:
                                print("It's a tie!")
                        break
                    
                    if letter == "o":
                        #Bot as X and player as O
                        #Plays the game with a max of 9 plays (for 9 spots on the board), ending when someone wins
                        for i in range(0, 4):
                            x_choice = check_bot_choice()
                            place_letter("X", x_choice)
                            if check_win("X") == "win":
                                print("You lose!")
                                break
                            o_choice = check_choice("O")
                            place_letter("O", o_choice)
                            if check_win("O") == "win":
                                print("You win!")
                                break
                            time.sleep(1) #waits a second before continuing
                        if check_win("O") != "win" and check_win("X") != "win":
                            x_choice = check_bot_choice("X")
                            place_letter("X", x_choice)
                            if check_win("X") == "win":
                                print("You lose!")
                            else:
                                print("It's a tie!")
                        break

                    else:
                        print("What?")
                break
            
            elif players == "2":
                #Two players against each other
                names = input("what are your names? (separated by a comma) ").split(",")
                #randomly assigns x and o to the players
                x_player = random.choice(names)
                while True:
                    o_player = random.choice(names)
                    if o_player != x_player:
                        break
                print(f"{x_player} plays as x, {o_player} plays as o")
                for i in board:
                    print(i)
                #Plays the game with a max of 9 plays (for 9 spots on the board), ending when someone wins
                for i in range(0, 4):
                    x_choice = check_choice("X")
                    place_letter("X", x_choice)
                    if check_win("X") == "win":
                        print(f"{x_player} wins!")
                        break
                    o_choice = check_choice("O")
                    place_letter("O", o_choice)
                    if check_win("O") == "win":
                        print(f"{o_player} wins!")
                        break
                if check_win("O") != "win" and check_win("X") != "win":
                    x_choice = check_choice("X")
                    place_letter("X", x_choice)
                    if check_win("X") == "win":
                        print(f"{x_player} wins!")
                    else:
                        print("It's a tie!")
                break
            
            else:
                print("What? ")
    
    elif play == "no":
        print("See ya!")
        break
    
    else:
        print("What?")
