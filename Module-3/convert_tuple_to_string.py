#Write a Python program to convert a tuple to a string.

list1 = []      #create list
tuple1 = ()     #create tuple
n = int(input("Enter number element : "))     #get value from user
String = ''   #Initialize empty string  
for i in range(n):
    input_element = input("Enter element : ")
    list1.append(input_element)     #add element in list

tuple1 = tuple(list1)   #convert list into tuple
for item in tuple1:
    String += item      #store character in string

print("Tuple is : ",tuple1)     #display tuple
print("String is : ",String)    #display string