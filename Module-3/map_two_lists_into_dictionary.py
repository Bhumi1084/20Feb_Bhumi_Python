#Write a Python program to map two lists into a dictionary.

key1 = []   #initialize list
value1 = []

k1 = int(input("Enter number of key : "))   #get value from user
v1 = int(input("Enter number of value : "))

if k1==v1:  #check no of key and value are equal or not
    for i in range(k1):
        input_key = input(f"Enter {i+1} key : ")    #get value from user
        key1.append(input_key)  #add key in a list
        input_value = input(f"Enter {i+1} value : ")
        value1.append(input_value)  #add value in a list

    list_to_dict = dict(zip(key1, value1))  #convert list into dict and zip the lists
    print(f"List to dictionary : {list_to_dict}")   #display map two lists into a dictionary

else:
    print("Please Enter key and value are equal..!")