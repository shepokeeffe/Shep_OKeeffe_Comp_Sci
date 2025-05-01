"""
Author: Shep O'Keeffe
Date: 5/1/25
Description: A simplified version of Battleship where the player and a bot take turns placing boats and firing bombs at each other's
boards. The game ends when one player runs out of boats or bombs.
Bugs: None
Sources: CS classes, Rami Rahman (testing)
"""
import random #library of functions for random number generation
import time #library of functions for time delays

def check_boat_choice(player_1_board):
    """
    desc: asks the user where they want to place one of their boats, checks if the spot is available, and places the boat if it is
    args: player_1_board (2D list representing the player's board)
    returns: None
    """
    while True:
        boat_choice = input("Where would you like to put a boat? ").upper()
        boat_choice = list(boat_choice) #converts the string to a list
        column = boat_choice[0]
        if ord(column) >= 65 and ord(column) <= 69: #checks if the first character is a letter from A-E
            column = int(chr(ord(column) - 16)) #converts the letter to a number from 0-4
            try:
                row = int(boat_choice[1])
                if row >= 1 and row <= 5:
                    if player_1_board[row][column] == "🌊":
                        break
                    else:
                        print("not an available spot")
                else:
                    print("A1, etc.")
            except ValueError:
                print("A1, etc.")
            except IndexError:
                print("A1, etc.")
        else:
            print("A1, etc.")
    player_1_board[row][column] = "🚢"

def check_bomb_choice(player_2_board, player_2_hidden_board):
    """
    desc: asks the user where they want to fire one of their bombs, checks if there's a boat there, and sinks that boat if it is
    args: player_2_board (2D list representing the opponent's board)
          player_2_hidden_board (2D list representing the opponent's hidden board)
    returns: "hit" if a boat is hit
    """
    while True:
        bomb_choice = input("Where would you like to fire? ").upper()
        bomb_choice = list(bomb_choice)
        column = bomb_choice[0]
        if ord(column) >= 65 and ord(column) <= 69:
            column = int(chr(ord(column) - 16))
            try:
                row = int(bomb_choice[1])
                if row >= 1 and row <= 5:
                    if player_2_board[row][column] == "🚢":
                        print("Hit!")
                        player_2_board[row][column] = "💥"
                        player_2_hidden_board[row][column] = "💥"
                        return "hit"
                    elif player_2_board[row][column] == "🌊":
                        print("Miss!")
                        player_2_board[row][column] = "❌"
                        player_2_hidden_board[row][column] = "❌"
                        break
                    else:
                        print("Spot unavailable or already guessed.")
                else:
                    print("A1, etc.")
            except ValueError:
                print("A1, etc.")
            except IndexError:
                print("A1, etc.")
        else:
            print("A1, etc.")

def check_bot_boat_choice(player_2_board):
    """
    desc: places the bot's boats randomly on the board
    args: player_2_board (2D list representing the opponent's board)
    returns: None
    """
    for i in range (0,4):
        while True:
            row = random.randrange(1,6) #randomly chooses a row from 1-5
            column = random.randrange(1,6) #randomly chooses a column from 1-5
            if player_2_board[row][column] == "🌊":
                break
        player_2_board[row][column] = "🚢"

def check_bot_bomb_choice(player_1_board):
    """
    desc: places the bot's bombs randomly on the board and checks if it hits a boat
    args: player_1_board (2D list representing the player's board)
    returns: "hit" if a boat is hit
    """
    while True:
        row = random.randrange(1,6)
        column = random.randrange(1,6)
        if player_1_board[row][column] == "🚢":
            print("Opponent hit!")
            player_1_board[row][column] = "💥"
            return "hit"
        elif player_1_board[row][column] == "🌊":
            print("Opponent miss!")
            player_1_board[row][column] = "❌"
            break

def main():
    """
    desc: main function that initializes the game, sets up the boards, and runs the game loop including the other functions
    args: None
    returns: None
    """
    player_1_board = [["  ", "A ", "B ", "C ", "D ", "E "], ["1", "🌊", "🌊", "🌊", "🌊", "🌊"], ["2", "🌊", "🌊", "🌊", "🌊", "🌊"], ["3", "🌊", "🌊", "🌊", "🌊", "🌊"], ["4", "🌊", "🌊", "🌊", "🌊", "🌊"], ["5", "🌊", "🌊", "🌊", "🌊", "🌊"]]
    player_2_board = [["  ", "A ", "B ", "C ", "D ", "E "], ["1", "🌊", "🌊", "🌊", "🌊", "🌊"], ["2", "🌊", "🌊", "🌊", "🌊", "🌊"], ["3", "🌊", "🌊", "🌊", "🌊", "🌊"], ["4", "🌊", "🌊", "🌊", "🌊", "🌊"], ["5", "🌊", "🌊", "🌊", "🌊", "🌊"]]
    player_2_hidden_board = [["  ", "A ", "B ", "C ", "D ", "E "], ["1", "🌊", "🌊", "🌊", "🌊", "🌊"], ["2", "🌊", "🌊", "🌊", "🌊", "🌊"], ["3", "🌊", "🌊", "🌊", "🌊", "🌊"], ["4", "🌊", "🌊", "🌊", "🌊", "🌊"], ["5", "🌊", "🌊", "🌊", "🌊", "🌊"]]
    player_boats = 4
    bot_boats = 4
    bombs = 10

    for i in range(0,4):
        print("Your board:")
        for i in player_1_board:
            print(" ".join(i)) #prints each row of the board (just the elements)
        check_boat_choice(player_1_board)
    print("Your board:")
    for i in player_1_board:
        print(" ".join(i))
    check_bot_boat_choice(player_2_board)
    print("Opponent's board:")
    for i in player_2_hidden_board:
        print(" ".join(i))
    print(f"You have {bombs} bombs.")
    while True:
        if player_boats == 0:
            print("You lose!")
            break
        elif bot_boats == 0:
            print("You win!")
            break
        elif bombs == 0:
            if player_boats > bot_boats:
                print("Out of bombs. You win!")
            elif player_boats < bot_boats:
                print("Out of bombs. You lose!")
            else:
                print("Out of bombs. It's a tie!")
            break
        else:
            if check_bomb_choice(player_2_board, player_2_hidden_board) == "hit":
                bot_boats -= 1
            bombs -=1
            for i in player_2_hidden_board:
                print(" ".join(i))
            print(f"Your opponent has {bot_boats} boat(s) left.")
            print(f"You have {bombs} bombs left.")
            time.sleep(2) #adds a delay of 2 seconds
            if check_bot_bomb_choice(player_1_board) == "hit":
                player_boats -= 1
            for i in player_1_board:
                print(" ".join(i))
            print(f"You have {player_boats} boat(s) left.")

main()

"""
key:
water/unknown = 🌊
boat = 🚢
hit = 💥
miss = ❌

algo:


CS2 Assignment
Dot Wars (Battleship)
Assignment: Build a simplified version of battleship.
Skills: 2D arrays, functions
Details:
1. Create a board of size 5x5 with 4 randomly placed dots.
2. Report the status of the board and how many turns you have left (start with 10)
3. Ask the user for coordinates to shoot at.
4. Tell the user what happened.

Note: For full credit, your code must be documented, properly indented, and declarations should be at the
top.
Bonus:
1. Make the dots into shapes (like battleship). 
2. Let the user choose the board size and number of dots.
3. Make the dots move one box in a random direction every round
4. Tell the user how close to the nearest dot their shot was.
5. Play sounds for hit; miss; kaboom
"""