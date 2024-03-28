#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = []     #Initialize list
n = int(input("Enter number of tuple : "))      #get value from user
for i in range(n):
    input_element = input(f"Enter a {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))     #add element and split the element

print(tuple1)   #display tuples from a list
for i in tuple1:
    if len(i)==0:
        tuple1.remove(i)   #remove blank tuple
        
print(tuple1)   #display empty tuples from a list of tuples