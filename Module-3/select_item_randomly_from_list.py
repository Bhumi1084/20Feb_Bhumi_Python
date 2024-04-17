#Write a Python program to select an item randomly from a list.

import random 

list1 = []  #initialize
n = int(input("Enter a number of element : "))      #get value from user

for i in range(n):
    element = input(f"Enter {i+1} element : ")
    list1.append(element)       #add element from list1

random_item = random.choice(list1)      #random choice element in a list1
print("Randomly item selected from a list : ",random_item)  #display randomly item from a list