#Write a Python program to check whether an element exists within a tuple.

list1 = []  #Initialize an empty list
n = int(input("Enter number of element : "))    #get value from the user

for i in range(n):
    list_input = input("Enter a element : ")
    list1.append(list_input)    #add an element in the list

tuple1 = tuple(list1)   #conver the list into tuple
#print(tuple1)
element = input("Enter a element to check : ")   #get value from user
if element in tuple1:   #Check if the element exists in the tuple
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exists in the tuple.")