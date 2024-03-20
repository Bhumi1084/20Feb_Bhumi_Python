#Write a Python program to convert a list to a tuple.

list1 = []
n = int(input("Enter a number of element : "))

for i in range(n):
    input_element = input("Enter a element : ")
    list1.append(input_element)

print("conver list into tuple : ",tuple(list1))