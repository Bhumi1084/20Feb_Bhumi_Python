#Write a python program to sum of the first n positive integers.

n=int(input("Enter possitive number : "))
sum=0
if n>0:
    for i in range(n):
        sum=sum+i
    print("Sum : ",sum)
else:
    print("Enter possitive number")