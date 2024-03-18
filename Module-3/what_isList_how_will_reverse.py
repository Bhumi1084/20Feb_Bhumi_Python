#What is List? How will you reverse a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

'''
Q : What is List?
=> List is a collection which is ordered and changeable.
=> Allows duplicate members.
=> The list is a sequence data type which is used to store the collection of data.

'''

#How will you reverse a list? Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 

list1 = []
n = int(input("Enter number of list element : "))

for i in range(n):
    input_element = input("Enter element : ")
    list1.append(input_element)

print("Input Element : ",list1)
print("list1 in [-1] is : ",list1[-1])
list1.reverse()
print("Reverse element : ",list1)