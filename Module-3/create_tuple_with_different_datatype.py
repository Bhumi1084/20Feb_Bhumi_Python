#Write a Python program to create a tuple with different data types.

tuple1 = []     #initialize 
n = int(input("Enter a number of element : "))  #get value from user

for i in range(n):
    input_element = input("Enter a element : ")
    if input_element.isdigit():
        input_element = int(input_element)     #convert string to digit
    tuple1.append(input_element)    #add element

print(tuple(tuple1))    #display tuple with different data type 