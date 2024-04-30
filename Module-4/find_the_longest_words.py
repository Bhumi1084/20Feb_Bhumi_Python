#Write a python program to find the longest words.

f = open("first.txt",'r')   #open file in read mode

max_length = 0  #initialize variable
longest_word = ""   #initialize variable

for line in f:
    words = line.strip().split()    #split the line
    for word in words:
        if len(word) > max_length:
            max_length = len(word)  #count length of word
            longest_word = word 
        elif len(word) == max_length:   
            longest_word += " " + word

print("Longest word : ",longest_word)   #display longest word