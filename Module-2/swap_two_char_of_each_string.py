# Write a Python program to get a single string from two given strings, separated by a space and swap the 
#first two characters of each string.

string1=input("Enter first string : ")      #get value from user    #abc
string2=input("Enter second string : ")     #xyz

start = string1[1]      #b
end = string1[0]    #a
swap_str1 = start+end+string1[2]    #bac

start = string2[1]  #y
end = string2[0]    #x
swap_str2 = start+end+string2[2]    #yxz

string = swap_str1 + " " + swap_str2    #bca yxz
print(string)   #display string