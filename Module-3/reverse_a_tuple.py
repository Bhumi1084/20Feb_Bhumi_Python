#Write a Python program to reverse a tuple.

list1 = []  #Initialize an empty list
n = int(input("Enter a element : "))    #get value from the user

for i in range(n):
    input_element = input("Enter an element : ")
    list1.append(input_element)     #add an element in the list

print("Tuple is : ",tuple(list1))
list1.reverse()     #reverse a list
reversed_tuple = tuple(list1)   #conver the list into tuple
print(f"Reversed Tuple : {reversed_tuple}")     #display reverse a tuple