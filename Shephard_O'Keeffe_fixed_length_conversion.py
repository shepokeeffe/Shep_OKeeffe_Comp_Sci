"""
Author: Shep O'Keeffe
Date: 3/7/25
Description: Converts a fixed-length file to a variable-length file
Bugs: None
Sources: CS classes
"""
student_data = open("student_data_cs2.txt")
csv_file = open('student_data.csv', 'w') #write mode
for line in student_data:
    csv_file.write(line[0:4].replace(" ","") + ',' + line[6:17].replace(" ","") + ',' + line[21:31].replace(" ","") + ',' + line[36:41].replace(" ","") + ',' + line[42:46].replace(" ","") + ',' + line[48:58].replace(" ","") + ',' + line[60:66].replace(" ","") + ',' + line[67:76].replace(" ","") + ',' + line[76:85].replace(" ","") + ',' + line[86:92].replace(" ","") + ',' + line[93:102].replace(" ","") + ',' + line[102:111].replace(" ","") + "\n") #adding the text without the spaces and comma-separated 