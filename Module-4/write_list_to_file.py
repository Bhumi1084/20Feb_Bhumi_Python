#Write a Python program to write a list to a file.

list1 = []  #initialize list

n = int(input("Enter number of element in list : "))    #get value from user
for i in range(n):
    element = input(f"Enter {i+1} element : ")  #get value from user
    list1.append(element)   #add value in list
    
f = open("first.txt","a")   #open file in append mode
for item in list1:
    f.write("\n"+list1)     #write in the file