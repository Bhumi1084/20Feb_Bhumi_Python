#Write a Python program to find the second smallest number in a list.
list1 = []
n = int(input("Enter number of element : "))    #get value from user

if n!=0:
    for i in range(n):
        list1_input = int(input("Enter a number : "))   
        list1.append(list1_input)   #add element in a list

    print(list1)
    lowest = min(list1)     #get the first lowest element from the list
    list1.remove(lowest)    #Remove the first lowest element from the list

    second_lowest = min(list1)  #Get the second lowest element from the list
    print("Second smallest element is : ",second_lowest)    #display second lowest element 
else:
    print("Enter valid number of element.")