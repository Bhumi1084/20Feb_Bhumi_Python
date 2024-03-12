#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

number1=int(input("Enter 1 Number : "))     #get value from user
number2=int(input("Enter 2 Number : "))
number3=int(input("Enter 3 Number : "))     

#check condition
#Here user enter any 2 number of zero then print this message Enter Proper value.
#condition are false then calculate the sum
if number1==0 and number2==0 or number1==0 and number3==0 or number2==0 and number3==0:
    print("Enter Proper value.")
else:
    total=number1+number2+number3
    print("Your Sum is : ",total)