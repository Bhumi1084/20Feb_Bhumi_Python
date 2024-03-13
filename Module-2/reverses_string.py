#Write a Python function to reverses a string if its length is a multiple of 4. 

string=input("Enter a string : ")
reverses_string = " "
index = len(string) - 1

while index >= 0:
    reverses_string += string[index]
    index -= 1
print(reverses_string)
