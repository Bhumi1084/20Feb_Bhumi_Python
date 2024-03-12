#Write a Python program to get the Factorial number of given number.

number=int(input("Enter a number : "))
fact=1
if number<0:
    print("Enter integer number.")
else:
    for i in range(1,number):
        fact=fact * i
        i+=1
    print("Factorial is : ",fact)