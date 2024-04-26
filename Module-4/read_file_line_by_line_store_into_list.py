#Write a Python program to read a file line by line and store it into a list.

f = open('first.txt','r')   #file open in read mode
lines = []  #initialize list

for line in f:
    lines.append(line)  #add lines in list
    
for line in lines:
    print(line)     #display file line by line

print("\n-----------------------Display In List-----------------------\n")
print(lines)    #display list