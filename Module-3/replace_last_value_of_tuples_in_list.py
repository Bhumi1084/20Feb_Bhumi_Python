#Write a Python program to replace last value of tuples in a list.

tuple1 = []     #initialize 
n = int(input("Enter number of tuple : "))      #get value from user
for i in range(n):
    input_element = input(f"Enter {i+1} tuple element : ")
    tuple1.append(tuple(input_element.split()))     #add value in a list

print(tuple1)   #display created list
updated_value = input("Enter update value : ")      #get value from user
for i in range(len(tuple1)):
    upd_list = list(tuple1[i])      #find and get last value in a tuple
    upd_list[-1] = updated_value    #get new value
    tuple1[i] =tuple(upd_list)      #update last value in a tuple

print(tuple1)   #display replace last value of tuple in a list