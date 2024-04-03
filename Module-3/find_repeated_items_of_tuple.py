#Write a Python program to find the repeated items of a tuple.

tuple1 = []     #initialize
n = int(input("Enter number of element : "))    #get value from user
for i in range(n):
    input_element = input(f"Enter {i+1} element : ")    #get value
    tuple1.append(input_element)    #add element in tuple1

print("Your Tuple : ",tuple(tuple1))    #display tuple1

temp = []   #initialize list
repeated_item = []  #initialize list

for i in tuple1:
    if i not in temp:
        temp.append(i)      #add element in temp list
    else:
        repeated_item.append(i)     #add repeated element in repeated_item list

print("Repeated Item : ",tuple(repeated_item))      #display repeated items of a tuple