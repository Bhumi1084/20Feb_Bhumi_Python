#Write a Python program to read first n lines of a file.

f = open("first.txt","r")   #open first.txt file in read mode
user_input = int(input("Enter Number Of Lines : ")) #get value from user
for i in range(user_input):
    lines = f.readline()    #read first n lines
    print(lines)    #display first n lines