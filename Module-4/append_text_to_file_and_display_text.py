#Write a Python program to append text to a file and display the text.

f = open('first.txt','a')   #create or open file
user_input = input("Enter Append Text : ")      #get value from user
f.write(f"\n{user_input}")  #write text in file

f1 = open("first.txt",'r') 
file_content = f1.read()    #read a file
print(file_content)     #display data