#Write a Python function to reverses a string if its length is a multiple of 4. 

string=input("Enter a string : ")       #get value from user    #bhumi
reverses_string = " "       #Initialize
index = len(string) - 1

while index >= 0:     #index is 4,3,2,1,0
    reverses_string += string[index]    #4,3,2,1,0 
    index -= 1      #first print i then m then u then h then b
print(reverses_string)      #display reverse string