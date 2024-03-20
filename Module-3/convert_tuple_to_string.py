#Write a Python program to convert a tuple to a string.

list1 = []
tuple1 = ()
n = int(input("Enter number element : "))
String = ''
for i in range(n):
    input_element = input("Enter element : ")
    list1.append(input_element)

tuple1 = tuple(list1)
for item in tuple1:
    String += item

print("Tuple is : ",tuple1)
print("String is : ",String)