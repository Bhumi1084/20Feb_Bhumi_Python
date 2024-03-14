#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#If the string length is less than 2, return instead of the empty string.

input_string = input("Enter a string: ")    #get string

#Check if the length of the string is less than 2
if len(input_string) < 2:
    result = ""     #display empty string
else:
    result = input_string[0:2] + input_string[-2:]

print("Result:", result)    #display string