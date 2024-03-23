# Write a Python function that takes two lists and returns true if they have at least one common member.

list1 = []  #create list
n1 = int(input("Enter number of element : "))   #get value from user

for i in range(n1):     
    element1 = input("Enter element : ")
    list1.append(element1)  #add value in the list

list2 = []
n2 = int(input("Enter number of element : "))

for i in range(n2):
    element2 = input("Enter element : ")
    list2.append(element2)  #add value in the list

for element in list1:
    if element in list2:
        print("True")
        print(f"one common member is : {element}")  #Display common member
        break
    else:
        print("False")