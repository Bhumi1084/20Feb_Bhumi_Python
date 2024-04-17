#How can you get a random number in python?

import random   

range1 = int(input("Enter start range : "))     #get value from user
range2 = int(input("Enter end range : "))

random_number = random.random()     #get random number
print("Random Number : ",random_number) #display random number

number = random.randint(range1,range2)  #get random number between given range
print("Random Number : ",number)    #display random number