#Write a Python program to convert a list of tuples into a dictionary. 

tuple1 = []     #Initialize list
n = int(input("Enter number of tuple : "))      #get value from user
for i in range(n):
    input_element = input(f"Enter a {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))     #add element and split the element

print(tuple1)  

if n>=2:
    print(dict(tuple1))