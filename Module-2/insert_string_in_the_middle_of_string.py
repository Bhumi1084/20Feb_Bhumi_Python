#Write a Python function to insert a string in the middle of a string.

string = input("Enter a string : ")     #get value from user
add_string = input("Enter a string to insert : ")

middle_string = len(string) // 2

#insert a string in the middle of a string
new_string = string[:middle_string] + add_string + string[middle_string:]
print("New String : ",new_string)   #Display string