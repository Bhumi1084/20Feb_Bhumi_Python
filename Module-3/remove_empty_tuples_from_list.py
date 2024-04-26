#Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple1 = []     #Initialize list

n = int(input("Enter number of tuple : "))      #get value from user
for i in range(n):
    input_element = input(f"Enter a {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))     #add element and split the element

print("\n------Display Orignal Tuple------\n",tuple1)

remove_empty = []   #initialize list
for i in tuple1:
    if i:
        remove_empty.append(i)  #add tuple in a list
print("\n------Remove Empty Tuple------\n",remove_empty,"\n")  #display empty tuples from a list of tuples