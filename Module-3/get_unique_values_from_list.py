#Write a Python program to get unique values from a list

list1 = []  #initialize
n = int(input("Enter a number of element : "))      #get value from user

for i in range(n):
    input_element = input("Enter a element : ")
    list1.append(input_element)     #add element in a list

unique_value = set(list1)   #conver list into set and remove duplicate element
print("Unique value : ",list(unique_value))     #convert set into list and display Unique value in a list