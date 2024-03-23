#Write a Python program to count the occurrences of each word in a given sentence

sentence=input("Enter a string : ")     #get value from user
substring = sentence.split()      #split a string
print("Total word in given sentence is : ",len(substring))  #count length of sub string