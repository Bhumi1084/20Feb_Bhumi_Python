#Write a Python program to find the highest 3 values in a dictionary.

data = {}   #initialize dictionary
list1 = []  #initialize list
n = int(input("Enter number of pairs:"))

for i in range(n):
    key=input("Enter Key's:")   #get key from user
    value=input("Enter Value's:")   #get value from user
    list1.append(value)     #add value in list
    data[key] = value   #add key and value in dictionary

print("Dictionary : ",data)     #display dictionary

for i in range(3):
    max_number = max(list1)     #find max value
    print(f"The {i+1} maximum number in the dic is :", max_number)  #display highest 3 value
    list1.remove(max_number)
    
