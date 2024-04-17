#Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.

list1 = []      #initialize list

n = int(input("Enter number of element : "))    #get rang of number from user

for i in range(n):
    element = int(input(f"Enter {i+1} element : "))     #get value from user
    list1.append(element)   #add element in a list

print("Your List Is : ",list1)      #display list
minimum = min(list1)    #find min number
maximum = max(list1)    #find max number

print(f"Minimum number : {minimum}")    #display minimum number
print(f"Maximum number : {maximum}")    #display maximum number