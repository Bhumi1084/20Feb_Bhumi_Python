#Write a python program to sum of the first n positive integers.

n=int(input("Enter possitive number : "))   #get value from user
sum=0
if n>0:
    for i in range(n):
        sum=sum+i   #calculate sum of n
    print("Sum : ",sum)     #display sum of n
else:
    print("Enter possitive number")