# How will you compare two lists?

list1 = []  #create list
list2 = []

n1 = int(input("Enter list1 number of element : "))     #get value from user
for i in range(n1):
    element1 = input("Enter element : ")      
    list1.append(element1)  #add element in the list

n2=int(input("Enter list2 number of element : "))
for i in range(n2):
    element2 = input("Enter element : ")
    list2.append(element2)

print("List 1 : ",list1)    #display first list
print("List 2 : ",list2)    #display second list

if list1==list2:    #check first list == second list
    print("List are equal.")    
else:
    print("List are not equal.")