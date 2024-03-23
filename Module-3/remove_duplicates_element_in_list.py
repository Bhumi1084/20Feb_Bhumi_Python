#Write a Python program to remove duplicates from a list.

list1 = []      #create a list
n = int(input("Enter number of element : "))    #get a value from user

for i in range(n):
    element = input("Enter element : ")
    list1.append(element)   #add a element in the list

print("without remove duplicates element in list : ",list1)     #display list, without remove duplicate element 
list2=set(list1)    #convert list into set 
print("with remove duplicates element in list",list(list2))     #display list, with remove duplicate element