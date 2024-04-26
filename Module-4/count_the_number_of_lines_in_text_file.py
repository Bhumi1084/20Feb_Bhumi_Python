#Write a Python program to count the number of lines in a text file.

f = open('first.txt','r')   #open file in read mode

lines = f.readlines()   #readlines in file
line = []   #initialization

for i in lines:
    line.append(i)      #add lines


line_count = len(line)      #count length of lines
print(line_count)   #display number of lines in a text file