#How Do You Check The Presence Of A Key In A Dictionary?

dict1 = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    dict1[key1] = value1    #add key and value in dict1

key_check = input("Enter check key name : ")    #get value from user

if key_check in dict1:  #check if input key in a dict1 or not
    print(f"The key {key_check} Presence in the dictionary.")     #display key already exists in a dictionary
else:
    print(f"The key {key_check} dose not Presence in the dictionary.")  #display key not exists in a dictionary