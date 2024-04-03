# Write a Python function that takes two lists and returns true if they have at least one common member.

def have_common_member(list1, list2):   #create a function
    for element in list1:
        if element in list2:
            print(f"one common member is : {element}")  #Display common member
            return True
    return False

list1 = []  #Initialize
n1 = int(input("Enter list1 number of element : "))   #get value from user

for i in range(n1):     
    element1 = input("Enter element : ")
    list1.append(element1)  #add value in the list

list2 = []  #Initialize
n2 = int(input("Enter list2 number of element : "))

for i in range(n2):
    element2 = input("Enter element : ")
    list2.append(element2)  #add value in the list

if have_common_member(list1, list2):    #call function
    print("true")
else:
    print("false")