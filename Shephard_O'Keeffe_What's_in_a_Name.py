"""
Author: Shep O'Keeffe
Date: 2/28/25
Description:
Bugs:
Sources:
"""

import random

def reverse(name):
    return name[::-1] 

def count_vowels(name,vowels):
    vowel_counts = {}
    for letter in name:
        if letter in vowels:
            if letter in vowel_counts:
                vowel_counts[letter] += 1
            else:
                vowel_counts[letter] = 1
    return vowel_counts

def count_consonants(name,consonants):
    consonant_counts = {}
    for letter in name:
        if letter in consonants:
            if letter in consonant_counts:
                consonant_counts[letter] += 1
            else:
                consonant_counts[letter] = 1
    return consonant_counts

def first_name(name):
    name = name.split(" ")
    name = name[0]
    if name == name[::-1]:
        return f"{name}, a palindrome!"
    else:
        return name

def middle_name(name):
    name = name.split(" ")
    return name[1:-1]

def last_name(name):
    name = name.split(" ")
    name = name[-1]
    if "-" in name:
        return f"{name}, a hyphenated name!"
    else:
        return name

def initials(name):
    initials = []
    name = name.split(" ")
    for word in name:
        initials.append(word[0])
    return initials

def main():
    
    vowels = ['a','e','i','o','u','y']

    consonants = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

    name = input("What is your name? ")
    
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

main()

"""
Done:
1. Reverse and display
2. Determine the number of vowels. You can prompt user for a particular vowel or
create subtotals of each.
3. Consonant frequency. Bonus: Subtotals of each consonant
4. Return first name. Return boolean if first name is a palindrome
5. Return middle name(s)
6. Return last name. Return boolean if last name contains a hyphen
7. Make initials from name
11. Build a menu (Bonus)

To-do:
8. Function to convert to lowercase
9. Function to convert to uppercase
10. Modify array to create a random name (mix up letters)

Bonus:
12. Return boolean if name contains a title/distinction (“Dr.”, “Sir”, “Esq”, “Ph.d”)
(Bonus)
13. Return full-name as a sorted array of characters (Bonus)
14. COME UP WITH YOUR OWN! (Bonus)
15. Secret Bonus ---See me
"""