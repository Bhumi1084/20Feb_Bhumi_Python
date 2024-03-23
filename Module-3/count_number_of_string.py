#Write a Python program to count the number of strings where the string length is 2 or more and the first and 
#last character are same from a given list of strings.

list1 = []  #create a list
n = int(input("Enter number of string : "))     #get value from user

for i in range(n):
    string = input("Enter a string : ")
    list1.append(string)    #add a string in the list

count = 0   #Initialize

for i in list1:
    #Check if the length of the string is 2 or more and if the first character is equal to the last character
    if len(i) >= 2 and i[0] == i[-1]:
        count += 1      #count first and last character are equal

#display Number of strings where first and last character are same
print("Number of strings where first and last character are same : ", count)