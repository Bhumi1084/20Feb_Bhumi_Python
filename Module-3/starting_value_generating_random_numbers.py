#How will you set the starting value in generating random numbers?

import random

start = int(input("Enter Starting value : "))#get value from user
end = int(input("Enter ending value : "))
random.seed(42)     #Set the seed value

random_number = random.randint(start,end)   #Generate random numbers

print(random_number)