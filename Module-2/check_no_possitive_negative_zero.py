#Write a Python program to check if a number is positive, negative or zero.

number=int(input("Enter a number : "))  #get value from user

if number>0:    #check condition -> number is grater then zeero
    print("Number is Possitive.")
elif number==0:     #check condition -> number is zero
    print("Number is Zero.")
else:
    print("Number is Negative.")