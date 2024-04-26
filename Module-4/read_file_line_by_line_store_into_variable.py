#Write a Python program to read a file line by line store it into a variable.

f = open('first.txt','r')   #open file in read mode
lines = f.readlines()   #read file

for i in lines:
    line = i    #read file in line by line and store in variable
    print(line)     #display file line by line store it into a variable
