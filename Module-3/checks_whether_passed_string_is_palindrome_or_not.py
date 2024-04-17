#Write a Python function that checks whether a passed string is palindrome or not.

def is_palindrome(s):   #create function
    #Remove non-alphanumeric characters and convert to lowercase
    cleaned_s = ''  #initialize variable
    for char in s:
        if char.isalnum():  
            cleaned_s += char.lower()   #convert lower case
    
    #Check if the string is equal to its reverse
    reversed_s = ''     #initialize variable
    for char in cleaned_s:
        reversed_s = char + reversed_s  #reversed string 
    if cleaned_s == reversed_s:
        print("The string is a palindrome.")    #display message
    else:
        print("The string is not a palindrome.")

# Test the function
string = input("Enter a string: ")  #get string from user
is_palindrome(string)       #call function