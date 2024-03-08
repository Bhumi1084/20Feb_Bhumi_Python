# Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
number = int(input("Enter a number : "))    #get value from user

if number%2==0:     #check number is even or odd
    print(f"{number} is Even.")
else:
    print(f"{number} is Odd.")      #print message
