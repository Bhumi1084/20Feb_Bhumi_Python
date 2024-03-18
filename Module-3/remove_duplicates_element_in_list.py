#Write a Python program to remove duplicates from a list.

list1 = []
n = int(input("Enter number of element : "))

for i in range(n):
    element = input("Enter element : ")
    list1.append(element)

print("without remove duplicates element in list : ",list1)
list2=set(list1)
print("with remove duplicates element in list",list(list2))