#Write a Python program to check multiple keys exists in a dictionary

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in a dict1

keys_check = []     #initialize
n2 = int(input("Enter number of check keys : "))    #get value from user

for i in range(n2):
    input_key = input(f"Enter {i+1} keys : ")
    keys_check.append(input_key)    #add key in a keys_check

print(dict1)
for key in keys_check:
    if key not in dict1:
        print(f"{key} does not exists in a dictionary.")    #display message for not exists key in a dictionary
    else:
        print(f"{key} exists in a dictionary.")     #display message for exists key in a dictionary