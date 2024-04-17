#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user

if n<=15:
    for i in range(n):
        key1 = input(f"Enter {i+1} Keys : ")    #get value
        value1 = input(f"Enter {i+1} Values : ")
        dict1[key1] = value1    #add key and value in dict1
    print(dict1)
else:
    print("Please! Enter number between 1 and 15.")