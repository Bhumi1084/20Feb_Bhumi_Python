#Write a Python program to convert a list of characters into a string.

char_list = []  #create list
n = int(input("Enter number of character : "))     #get value from user
string = ''     #Initialize empty string

#Loop to input characters and add the list
for i in range(n):
    input_char = input("Enter character : ")
    char_list.append(input_char)
    #string += i

for item in char_list:
    string += item  #character store in the string

print("List is : ",char_list)   #display  list
print("String is : ",string)    #display string