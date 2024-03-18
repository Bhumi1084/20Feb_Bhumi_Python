#Write a Python program to check a list is empty or not.

list1 = []
n = int(input("Enter number of element : "))

for i in range(n):
    element = input("Enter element : ")
    list1.append(element)


if len(list1) == 0:
    print("list is empty.")
else:
    print("List : ",list1)
    print("list is not empty.")