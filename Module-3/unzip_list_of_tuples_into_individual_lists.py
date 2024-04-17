#Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]     #declare list of tuple

#Initialize empty lists
list1 = []
list2 = []

#Unzip the list of tuples into individual lists
for tuple1 in list_of_tuples:
    list1.append(tuple1[0])    #add first value in a list1
    list2.append(tuple1[1])   #add second value in a list2

#display unzip a list of tuples into individual lists
print("First elements:", list1) 
print("Second elements:", list2)