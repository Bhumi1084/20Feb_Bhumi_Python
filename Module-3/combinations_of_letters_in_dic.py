#Write a Python program to create and display all combinations of letters, 
#selecting each letter from a different key in a dictionary.  
#Sample data: {'1': ['a','b'], '2': ['c','d']}  
#Expected Output:  
#   ac ad bc bd 

data = {'1': ['a', 'b'], '2': ['c', 'd']}   #create dictionary
result = []
#Generate and print all combinations
for i in data['1']:
    for j in data['2']:
        result.append(i+j)  #add element in list

print(result)   #display result