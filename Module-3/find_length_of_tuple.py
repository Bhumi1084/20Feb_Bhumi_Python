#Write a Python program to find the length of a tuple.

list1 = []      #create a list
tuple1 = ()     #create a tuple
n = int(input("Enter number element : "))   #get a value from user

for i in range(n):
    input_element = input("Enter element : ")
    list1.append(input_element)     #add element in list

tuple1 = tuple(list1)   #convert list into tuple
print("Length of tuple is : ",len(tuple1))  #display tuple