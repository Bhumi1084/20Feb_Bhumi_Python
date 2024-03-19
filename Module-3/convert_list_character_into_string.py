#Write a Python program to convert a list of characters into a string.

char_list = []
n = int(input("Enter number of character : "))
string = ''
for i in range(n):
    input_char = input("Enter character : ")
    char_list.append(input_char)
    #string += i

for item in char_list:
    string += item

print("List is : ",char_list)
print("String is : ",string)