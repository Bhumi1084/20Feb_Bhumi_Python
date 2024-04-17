#Write a Python program to read a random line from a file.

import random

f1 = open('temp.txt','w')   #create file and write in file

n = int(input("Enter number of student : "))    #get value from user
for i in range(n):
    id = int(input(f"Enter {i+1} id : "))   #get id from user
    name = input("Enter name : ")  #get name from user
    f1.write(f"Id : {id} \nName : {name} \n")   #write in temp.txt file
f1.close()

r1 = open('temp.txt','r+')      #open file   
lines = r1.readline()
random_line = random.choice(lines)
print("Random line from file : ",random_line)
r1.close()