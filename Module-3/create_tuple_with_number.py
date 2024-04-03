#Write a Python program to create a tuple with numbers.

tuple1 = []
n = int(input("Enter a number of element : "))

for i in range(n):
    input_element = input("Enter a element : ")
    if input_element.isdigit():
        input_element = int(input_element)
    tuple1.append(input_element)

print("Tuple with number is : ",tuple(tuple1))