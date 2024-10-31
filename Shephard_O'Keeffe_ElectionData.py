'''
Author: Shep O'Keeffe
Date: 10/31/24
Description: Takes a speech by Donald Trump and one by Kamala Harris and puts the top 15 most common words from each (barring excessively common words such as "the" or "is") into a csv file from which they can be plotted into a graph through excel.
Bugs: none
Sources: computer science classes, geeksforgeeks.org
'''
t_speech = open('cleaned_trump_speech_transcript.txt')
t_word_d = {}
t_bad_words = ['', 'the', 'and', 'to', 'of', 'our', 'will', 'in', 'we', 'a', 'i', 'have', 'is', 'that', 'are', 'for', 'it', 'this', 'on', 'my', 'you', 'be', 'their', 'with', 'by', 'has', 'who', 'not', 'was', 'they', 'going', 'from', 'so', 'been', 'at', 'all', 'them', 'but', 'no', 'she', 'your', 'ever', 'one', 'am', 'than', 'these', 'again', 'every', 'its', 'were', 'or', 'can', 'other', 'her', 'what', 'as', 'when', 'an', 'because', 'out', 'never', 'us', 'also', 'way', 'which', 'me', 'years', 'make', 'time', 'year', 'now', 'new', 'more']
for line in t_speech:
    line = line.lower()
    line = line.replace(","," ")
    line = line.replace("."," ")
    line = line.replace("!"," ")
    line = line.replace("?"," ")
    line = line.replace(";"," ")
    line = line.replace(":"," ")
    t_words = line.split(' ')
    for word in t_words:
        if word in t_word_d:
            t_word_d[word] += 1
        else:
            t_word_d[word] = 1
t_sorted_dict = dict(sorted(t_word_d.items(), key=lambda item: item[1], reverse = True)) #sorts the words in the dictionary by value in descending order
for word in t_bad_words: 
    if word in t_sorted_dict:
        del t_sorted_dict[word]
print(t_sorted_dict)
file = open('trump_data.csv', 'w') #opens the new file in writing mode
for key,value in t_sorted_dict.items():
    if value >= 10:
        file.write(key + ',' + str(value) + '\n') #enters the keys and values into the file, separated by commas, adding new lines between each pair

h_speech = open('kamala_new.txt')
h_word_d = {}
h_bad_words = ['it', 'this', 'an', 'when', 'have', 'has', 'but', 'would', 'was', 'one', 'their', 'me', 'all', 'know', 'they', 'his', 'about', 'up', 'at', 'because', 'out', 'what', 'so', 'from', 'always', 'let', 'by', 'never', 'your', 'like']
for line in h_speech:
    line = line.lower()
    line = line.replace(","," ")
    line = line.replace("."," ")
    line = line.replace("!"," ")
    line = line.replace("?"," ")
    line = line.replace(";"," ")
    line = line.replace(":"," ")
    h_words = line.split(' ')
    for word in h_words:
        if word in h_word_d:
            h_word_d[word] += 1
        else:
            h_word_d[word] = 1
h_sorted_dict = dict(sorted(h_word_d.items(), key=lambda item: item[1], reverse = True))
for word in h_bad_words: 
    if word in h_sorted_dict:
        del h_sorted_dict[word]
print(h_sorted_dict)
file = open('harris_data.csv', 'w')
for key,value in h_sorted_dict.items():
    if value >= 8 and value <= 17:
        file.write(key + ',' + str(value) + '\n')