#Write a Python program that will return true if the two given integer values are equal or their sum or 
#difference is 5.

number1=int(input("Enter 1 number : "))     #get value from user
number2=int(input("Enter 2 number : "))

sum=number1+number2     #calculate addition
print("Sum : ",sum)     #display sum
difference=number2-number1      #calculate the difference
print("Difference : ",difference)   #display difference

if number1==number2 or sum==5 or difference==5:     #condition are true then return true
    print("True")
else:
    print("False")