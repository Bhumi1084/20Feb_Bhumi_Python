'''
Write a Python program to combine values in python list of dictionaries. 
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
300}, o {'item': 'item1', 'amount': 750}] 
Expected Output:
Counter ({'item1': 1150, 'item2': 300}) 
'''

data = []   #initialize list

#Get input data from the user
n = int(input("Enter the number of items: "))

for i in range(n):
    item_name = input(f"Enter the name of item {i+1} : ")
    item_amount = int(input(f"Enter the amount for item {i+1} : "))
    data.append({'item' : item_name, 'amount' : item_amount})

result = {} #Initialize an empty dictionary to store combined values

#Combine values from the list of dictionaries
for d in data:
    item = d['item']
    amount = d['amount']
    if item in result:
        result[item] += amount
    else:
        result[item] = amount

print(result)   #display combine values in list of dictionaries