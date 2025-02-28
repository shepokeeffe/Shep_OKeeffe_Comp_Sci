"""
Author: Shep O'Keeffe
Date: 2/28/25
Description: A number of string functions built from scratch. The user enters their name and selects how they wish for it to be modified.
Bugs: Counts titles such as Dr. or Esq. as first or last names
Sources: CS classes
"""

import random

def reverse(name):
    """
    Description: Puts the letters of the name into reverse order
    Args: 
        name - The user's name
    Returns: The user's name in reverse
    """
    return name[::-1] 

def count_vowels(name,vowels):
    """
    Description: Finds the number of times different vowels appear in the user's name
    Args:
        name - The user's name
        vowels - List of vowels
    Returns: Number of times each vowel appears
    """
    vowel_counts = {}
    for letter in name:
        if letter in vowels:
            if letter in vowel_counts:
                vowel_counts[letter] += 1
            else:
                vowel_counts[letter] = 1
    return vowel_counts

def count_consonants(name,consonants):
    """
    Description: Finds the number of times different consonants appear in the user's name
    Args:
        name - The user's name
        consonants - List of consonants
    Returns: Number of times each consonant appears
    """
    consonant_counts = {}
    for letter in name:
        if letter in consonants:
            if letter in consonant_counts:
                consonant_counts[letter] += 1
            else:
                consonant_counts[letter] = 1
    return consonant_counts

def first_name(name):
    """
    Description: Finds the user's first name
    Args:
        name - The user's name
    Returns: The user's first name (bonus: notes if the name is a palindrome)
    """
    name = name.split(" ")
    name = name[0]
    if lowercase(name) == reverse(lowercase(name)):
        return f"{name}, a palindrome!"
    else:
        return name

def middle_name(name):
    """
    Description: Finds the user's middle name(s)
    Args:
        name - The user's name
    Returns: The user's middle name(s)
    """
    name = name.split(" ")
    return ' '.join(name[1:-1])

def last_name(name):
    """
    Description: Finds the user's last name
    Args:
        name - The user's name
    Returns: The user's last name (bonus: notes if the name is hyphenated)
    """
    name = name.split(" ")
    name = name[-1]
    if "-" in name:
        return f"{name}, a hyphenated name!"
    else:
        return name

def initials(name):
    """
    Description: Finds the user's initials
    Args:
        name - The user's name
    Returns: The user's initials
    """
    initials = []
    name = name.split(" ")
    while True:
        if "" in name:
            name.remove("")
        else:
            break
    for word in name:
        initials.append(uppercase(word[0]))
    return ' '.join(initials)

def lowercase(name):
    """
    Description: Puts the user's name into lowercase
    Args:
        name - The user's name
    Returns: The user's name in lowercase
    """
    lower_name = []
    for letter in name:
        if ord(letter) >= 97 and ord(letter) <= 122:
            lower_name.append(letter)
        elif ord(letter) >= 65 and ord(letter) <= 90:
            letter = chr(ord(letter) + 32)
            lower_name.append(letter)
        else:
            lower_name.append(letter)
    return ''.join(lower_name)

def uppercase(name):
    """
    Description: Puts the user's name into uppercase
    Args:
        name - The user's name
    Returns: The user's name in uppercase
    """
    upper_name = []
    for letter in name:
        if ord(letter) >= 65 and ord(letter) <= 90:
            upper_name.append(letter)
        elif ord(letter) >= 97 and ord(letter) <= 122:
            letter = chr(ord(letter) - 32)
            upper_name.append(letter)
        else:
            upper_name.append(letter)
    return ''.join(upper_name)

def randomize(name):
    """
    Description: Randomizes the letters of the user's name
    Args:
        name - The user's name
    Returns: The letters of the user's name in random order
    """
    randomized_word = []
    name = list(name)
    for i in range(len(name)):
        random_letter = random.choice(name)
        name.remove(random_letter)
        randomized_word.append(random_letter)
    return ''.join(randomized_word)

def main():
    
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']

    consonants = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','R','T','P','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

    name = input("What is your name? ")

    while True:

        menu = input("""Would you like me to:

1. Reverse your name
2. Count the vowels in your name
3. Count the consonants in your name
4. Find your first name
5. Find your middle name(s)
6. Find your last name
7. Find your initials
8. Put your name into lowercase
9. Put your name into uppercase
10. Randomize the letters of your name
0. Quit

""")

        #calling all functions

        if menu == "1":
            print(reverse(name))
        
        elif menu == "2":
            print(count_vowels(name,vowels))

        elif menu == "3":
            print(count_consonants(name,consonants))

        elif menu == "4":
            print(first_name(name))

        elif menu == "5":
            print(middle_name(name))

        elif menu == "6":
            print(last_name(name))

        elif menu == "7":
            print(initials(name))

        elif menu == "8":
            print(lowercase(name))

        elif menu == "9":
            print(uppercase(name))

        elif menu == "10":
            print(randomize(name))

        elif menu == "0":
            break

main()
