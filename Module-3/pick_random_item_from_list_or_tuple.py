#How can you pick a random item from a list or tuple?

import random

list1 = []  #initialize list
n = int(input("Enter number of element : "))    #get value from user

for i in range(n):
    element = input(f"Enter {i+1} element : ")  
    list1.append(element)   #add element in list

random_item = random.choice(list1)  #select random element in the list
print("Your Random Item Is : ",random_item) #display random element