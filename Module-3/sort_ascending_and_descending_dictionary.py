#Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {}  #initialize dict1
n=int(input("Enter number of dict1 pairs : "))  #get value from user
for i in range(n):
    key1 = input(f"Enter {i+1} Keys : ")    #get value
    value1 = input(f"Enter {i+1} Values : ")
    my_dict[key1] = value1    #add key and value in a dict1

asc = sorted(my_dict.values())     #sort value in ascending order
#desc = asc.reverse()
desc = asc[-1:]         #sort value in descending order

print("Value sorted in ascending order:", asc)          #display ascending order
print("Value sorted in descending order:", desc)        #display descending order