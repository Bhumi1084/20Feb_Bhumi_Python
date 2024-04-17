#Write a Python program to combine two dictionary adding values for common keys. 
#d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1) 
        dict1[key1] = value1
    else:
        dict1[key1] = value1

dict2 = {}  #initialize dict1
n=int(input("Enter number of dict2 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    if value1.isdigit():
        value1 = int(value1)
        dict2[key1] = value1
    else:
        dict2[key1] = value1

#Combining dictionaries and adding values for common keys
combined_dict = {}      #initilize

#Add values in combined_dict from dict1
for key, value in dict1.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

#Add values in combined_dict from dict2
for key, value in dict2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print(dict1)    #display first dictionary
print(dict2)    #display second dictionary
print("Combined dictionary : ", combined_dict)      #display combine two dictionary adding values for common keys