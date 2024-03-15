#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given 
#string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, 
#leave it unchanged.

string = input("Enter a string : ")     #get value from user

if len(string) >= 3:    
    if string.endswith("ing"):      #string end with ing 
        new_string = string + "ly"  #add ly
    else:
        new_string = string + "ing"     #add ing
else:
    new_string = string     

print("Your New String : ",new_string)      #display new string