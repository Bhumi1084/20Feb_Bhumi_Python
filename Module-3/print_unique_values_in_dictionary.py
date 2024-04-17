#Write a Python program to print all unique values in a dictionary.

dict1 = {}
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in a dict1

# Creating a set to store unique values
unique_values = set()

# Iterating over the values in the dictionary and adding them to the set
for value in dict1.values():
    unique_values.add(value)

# Printing the unique values
print("Unique values in the dictionary : ", unique_values)
