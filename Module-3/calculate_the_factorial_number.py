#Write a Python function to calculate the factorial of a number (a nonnegative integer)

def factorial(n):   #create function
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i     #calculate factorial
        print("Factorial is : ", result)    #display factorial

number = int(input("Enter a number : "))    #get value from user
factorial(number)   #call function