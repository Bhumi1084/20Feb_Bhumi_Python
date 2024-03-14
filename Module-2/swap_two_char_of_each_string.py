# Write a Python program to get a single string from two given strings, separated by a space and swap the 
#first two characters of each string.

string1=input("Enter first string : ")
string2=input("Enter second string : ")

start = string1[1]
end = string1[0]
swap_str1 = start+end+string1[2]

start = string2[1]
end = string2[0]
swap_str2 = start+end+string2[2]

string = swap_str1 + " " + swap_str2
print(string)