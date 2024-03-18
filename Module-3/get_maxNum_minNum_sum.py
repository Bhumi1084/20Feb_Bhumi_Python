#Write a Python function to get the largest number, smallest num and sum of all from a list.

list1 = []
n = int(input("Enter number of element : "))

for i in range(n):
    element = int(input("Enter a element : "))
    list1.append(element)

largest = list1[0]
smallest = list1[0]
total_sum = 0

for num in list1:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    total_sum += num

print("\nLargest Number : ",largest)
print("Smallest Number : ",smallest)
print("Total sum : ",total_sum)