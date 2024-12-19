"""
Author: Shep O'Keeffe
Date: 12/20/24
Description: Hangman. Player guesses the letters in a word randomly selected from a list of 500 8-letter words and 20 10-letter "challenge words."
Bugs: none
Sources: CS classes, Stack Overflow
"""
import random #used for random functions
#hangman graphics
gallows = [
'''
  +---+
      |
      |
      |
  --------
''',
'''
  +---+
  0   |
      |
      |
  --------
''',
'''
  +---+
  0   |
  |   |
      |
  --------
''',
'''
  +---+
  0   |
 /|   |
      |
  --------
''',
'''
  +---+
  0   |
 /|\  |
      |
  --------
''',
'''
  +---+
  0   |
 /|\  |
 /    |
  --------
''',
'''
  +---+
  0   |
 /|\  |
 / \  |
  --------
'''
]
#importing words
word_list = open('Shep_Hangman_words.txt') #opens the file
word_list = word_list.read() #sets the file to read mode
word_list = word_list.split('\n') #creates a list of each line in the file

while True:
  wanna_play = input("Wanna play hangman? ").lower()
  #setup for game
  if wanna_play == "yes" or wanna_play == "y":
    random_word = random.choice(word_list).lower() #takes a random word from the list and makes the letters lowercase
    character_guesses = []
    wrong_letters = []
    lives_lost = 0
    print(gallows[lives_lost]) #prints the item whose index matches the number of lives lost
    #challenge word feature
    if len(random_word) == 10:
      print("Challenge word!")
    #game
    while lives_lost < 6:                
      game_word = []
      unknown = 0        
      #setup for display
      for character in random_word:            
        if character in character_guesses:
          game_word.append(character)            
        else:
          game_word.append("_")
          unknown += 1
      #win condition (all letters guessed)
      if unknown == 0:
        print(f"The word was {random_word}!")
        print("You won!")
        break
      #display
      print(f"Incorrect guesses: {', '.join(wrong_letters)}") #prints each item in the list joined by ", "
      print(f"Word: {' '.join(game_word)}") #prints each item in the list joined by " "
      print("")
      player_choice = input("Guess the word or a letter: ").lower()
      print("")
      character_guesses.append(player_choice)
      #win condition (word guessed)
      if player_choice == random_word:
        print(f"The word was {random_word}!")
        print("You won!")
        break
      #wrong condition
      if player_choice not in random_word:
        #new wrong guess
        if player_choice not in wrong_letters:
          lives_lost += 1
          print("Wrong!")
          print(gallows[lives_lost])
          wrong_letters.append(player_choice)
        #guessed letter
        else:
          print("Character already guessed.")
      #lose condition
      if lives_lost == 6:
          print("You lost!")
          print(f"The word was {random_word}.")
  
  elif wanna_play == "no" or wanna_play == "n":
    print("Ok")
    break

  else:
    print("Huh?")