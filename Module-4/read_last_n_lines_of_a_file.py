#Write a Python program to read last n lines of a file. 

f = open('first.txt','r')   #open file in read mode
user_input = int(input("Enter Number Of Lines : "))     #get value from user
lines = f.readlines()   #read lines of file
last_n_lines = lines[-user_input:]  #read last n lines of file

for line in last_n_lines:
    print(line)     #display last n lines of a file