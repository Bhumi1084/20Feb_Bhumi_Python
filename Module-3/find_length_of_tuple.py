#Write a Python program to find the length of a tuple.

list1 = []
tuple1 = ()
n = int(input("Enter number element : "))

for i in range(n):
    input_element = input("Enter element : ")
    list1.append(input_element)

tuple1 = tuple(list1)
print("Length of tuple is : ",len(tuple1))