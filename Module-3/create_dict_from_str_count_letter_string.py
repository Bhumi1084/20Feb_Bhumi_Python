'''
Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string. 
Sample string: 'w3resource' 
Expected output: 
{'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

'''

string = input("Enter a string : ")     #get string from a user
letter_count = {}   #initialize dict

#Iterate through each character in the string
for char in string:
    if char in letter_count:    #Check if the character is already in the dictionary
        letter_count[char] += 1
    else:   #If not, add it to the dictionary with count 1
        letter_count[char] = 1

print("Output : ",letter_count)     #display string