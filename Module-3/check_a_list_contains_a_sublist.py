#Write a Python program to check whether a list contains a sub list.

main_list = []  #initialize list
sublist = []

n = int(input("Enter main list number of element : "))  #get value from user
n1 = int(input("Enter sublist number of element : "))

for i in range(n):
    element = input(f"Enter {i+1} main list element : ")
    main_list.append(element)   #add value in mainList list
    
for i in range(n1):
    element = input(f"Enter {i+1} sublist element : ")
    sublist.append(element)     #add value in sublist

#Convert lists to sets for intersection
main_set = set(main_list)
sublist_set = set(sublist)

#Check if the intersection of sets is equal to the sublist set
contains_sublist = sublist_set.intersection(main_set) == sublist_set

print(contains_sublist)  #display result