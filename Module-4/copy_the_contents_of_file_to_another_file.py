# Write a Python program to copy the contents of a file to another file.

f1 = open("first.txt","r")  #opent file in read mode
content = f1.read()     #read the file

f2 = open("copyFile.txt","a")   #open file in writemode
f2.write(content)   #write and copy the file

print("copied successfully...!!")   #print message