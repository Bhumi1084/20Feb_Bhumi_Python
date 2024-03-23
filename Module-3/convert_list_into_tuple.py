#Write a Python program to convert a list to a tuple.

list1 = []  #create list
n = int(input("Enter a number of element : "))  #get value from user

for i in range(n):
    input_element = input("Enter a element : ")
    list1.append(input_element)     #add element in list

print("conver list into tuple : ",tuple(list1))     #conver list into tuple and display result