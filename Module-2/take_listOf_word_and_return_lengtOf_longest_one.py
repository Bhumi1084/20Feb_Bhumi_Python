#Write a Python function that takes a list of words and returns the length of the longest one.

number = int(input("Enter total number of words : "))   #get value from user  #3
wordList = []
maxlength = 0
longest_words = []

for word in range(number):
    word = input(f"Enter {word+1} word : ")
    wordList.append(word)       #['this','is','python']

for word in wordList:
    if len(word) > maxlength:       #word=this,is,python
        maxlength = len(word)       #store maxlength in word       #4,2,6      
        longest_words = [word]      #Reset the list with the new longest word
    elif len(word) == maxlength:         
        longest_words.append(word)      #add another word with the same length

#print("Length of the longest word is :", maxlength) 
print("Longest word :", longest_words)