#Differentiate between append () and extend () methods?

'''
=> append() - add single element in the end of the list.
=> extend() - add a list in the end of the another list.

=> append() - takes one element as argument.
=> extend() - takes one list as argument.

=> append() - the length of the list will increase by 1.
=> extend() - the length of the list will increase by the length of inserted list.
'''
#example of append():

data = []   #create a list
n = int(input("Enter number of element : "))
for i in range(n):
    element = input("Enter a element : ")
    data.append(element)    #add one element in a list
print(data)     #display list

#example of extend():

data1 = []  
n1 = int(input("Enter number of element : "))
for i in range(n1):
    element1 = input("Enter a element : ")
    data1.append(element1)    #add one element in a list

data.extend(data1)       #Extend the first list with the elements of the second list
print(data)     #display first list