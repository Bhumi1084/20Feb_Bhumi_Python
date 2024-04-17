#Write a Python script to merge two Python dictionaries.

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in a dict1

dict2 = {}  #initialize dict2
n=int(input("Enter number of dict2 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in a dict2

concate_dict = {}   #initialize
list1 = [dict1, dict2]  #create list
for i in list1: 
    for key, value in i.items():    #all item from dict1 and dict2
        concate_dict[key] = value   #add key and value in a concate_dict

print("concatenate dictionaries : ",concate_dict)     #display concatenate dictionaries