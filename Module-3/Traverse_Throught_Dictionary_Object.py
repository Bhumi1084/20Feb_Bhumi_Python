#How Do You Traverse Through A Dictionary Object In Python?

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in dict1

for keys, values in dict1.items():
    print(keys, ":", values)    #display keys and values