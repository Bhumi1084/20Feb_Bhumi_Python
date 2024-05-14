#Write a Python program to count the frequency of words in a file.

word_freq = {}      #initialize
#file_name = input("Enter the file name: ")      #get value from user
f = open('first.txt', 'r')     #open file in read mode
for line in f:  
    words = line.split()  
    for word in words:                
        word = word.strip('.,?!;:"')  
        word = word.lower()    #convert lower case
        word_freq[word] = word_freq.get(word, 0) + 1    #count frequency of word

print("Word frequency:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")    #display word frequency of word