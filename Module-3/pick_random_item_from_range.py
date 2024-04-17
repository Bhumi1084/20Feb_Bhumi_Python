#How can you pick a random item from a range?

import random

start = int(input("Enter start range : "))  #get value from user
end = int(input("Enter end range : "))

my_range = range(start, end)    #give a range

#Convert range to a list and pick a random item
random_item = random.choice(list(my_range))

print("Random item from the range:", random_item)   #display random item from a range
