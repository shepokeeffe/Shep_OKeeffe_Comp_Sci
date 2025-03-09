"""
Author: Shep O'Keeffe
Date: 3/8/25
Description: Takes a text file representing an email inbox and finds the most frequent email sender, the number of emails sent during
each hour of the day, and the frequency of each letter of the alphabet.
Bugs: the list of hour frequencies from mbox.txt contains two elements that are not hours of the day
Sources: CS classes, PY4E
"""
uname_frequencies = {}
hour_frequencies = {}
letter_frequencies = {}

uname_count_tuples = []
hour_count_tuples = []
letter_count_tuples = []

while True:
    file_choice = input("Enter a file name: ")
    if file_choice == "mbox.txt" or file_choice == "mbox_short.txt":
        mbox = open(file_choice)
        for line in mbox:
            words = line.split(" ")
            if "From" in words:
                uname = words[1]
                if uname in uname_frequencies:
                    uname_frequencies[uname] += 1
                else:
                    uname_frequencies[uname] = 1
                time = words[6]
                hour = time.split(":")[0]
                if hour in hour_frequencies:
                    hour_frequencies[hour] += 1
                else:
                    hour_frequencies[hour] = 1
            for word in words:
                for letter in word:
                    if ord(letter) >= 97 and ord(letter) <= 122:
                        if letter in letter_frequencies:
                            letter_frequencies[letter] += 1
                        else:
                            letter_frequencies[letter] = 1

        sorted_uname_frequencies = dict(sorted(uname_frequencies.items(), key=lambda item: item[1], reverse = True))
        for key,value in sorted_uname_frequencies.items():
            uname_count_tuples.append(f"{key, value}")
        print(uname_count_tuples[0])

        sorted_hour_frequencies = dict(sorted(hour_frequencies.items(), key=lambda item: item[0]))
        for key,value in sorted_hour_frequencies.items():
            hour_count_tuples.append(f"{key, value}")
        for count_tuple in hour_count_tuples:
            print(count_tuple)

        sorted_letter_frequencies = dict(sorted(letter_frequencies.items(), key=lambda item: item[1], reverse = True))
        for key,value in sorted_letter_frequencies.items():
            letter_count_tuples.append(f"{key, value}")
        for count_tuple in letter_count_tuples:
            print(count_tuple)
        
        break
    
    else:
        print("please choose either mbox.txt or mbox_short.txt")
