#How will you create a dictionary using tuples in python?

list1 = []      #initialize
n = int(input("Enter number of tuple : "))      #get value from user

for i in range(n):
    input_element = input(f"Enter {i+1} tuple element : ")      #get value from user
    list1.append(tuple(input_element.split()))      #add element in list and convert in tuple

print(list1)    #display list of tuple
dictionary = dict(list1)    #convert tuple into dictionary
print(dictionary)   #display dictionary