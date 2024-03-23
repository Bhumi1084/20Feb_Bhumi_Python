#Write a Python function to get the largest number, smallest num and sum of all from a list.

list1 = []  #create list
n = int(input("Enter number of element : "))    #get a value from user

for i in range(n):
    element = int(input("Enter a element : "))  
    list1.append(element)   #add a element in the list

largest = list1[0]  #store the first element is the largest initially
smallest = list1[0]     #store the first element is the smallest initially
total_sum = 0   #store the total sum

for num in list1:
    if num > largest:
        largest = num   #Update largest value if current number is greater
    if num < smallest:
        smallest = num  #Update smallest value if current number is smaller
    total_sum += num    #calculate total sum

print("\nLargest Number : ",largest)    #display largest value
print("Smallest Number : ",smallest)    #display smallest value
print("Total sum : ",total_sum)     #display total sum