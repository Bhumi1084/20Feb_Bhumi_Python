#Write a Python program to check a list is empty or not.

list1 = []  #create list
n = int(input("Enter number of element : "))    #get value from user

for i in range(n):    
    element = input("Enter element : ")     #get value from user
    list1.append(element)   #add value in the list

demo = n.count(list1)
if len(list1) == 0:
    print("list is empty.")   #print message
elif demo == 0:
    print("clear")
else:
    print("List : ",list1)
    print("list is not empty.")