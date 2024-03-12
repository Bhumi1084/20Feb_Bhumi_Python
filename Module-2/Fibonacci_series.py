#Write a Python program to get the Fibonacci series of given range.

number=int(input("Enter the number of terms : "))
number1=0
number2=1
for i in range(1,number):
    if i<=1:
        number3=i
    else:
        number3 = number1 + number2
        number1 = number2
        number2 = number3
    print(number3)