#Write a Python program to get the Factorial number of given number.

number=int(input("Enter a number : "))      #get value from user
fact = 1    #Initialize
if number<0:    #check less then zero condition are true then print message
    print("Enter integer number.")
else:   #condition are false then calculate factorial number
    for i in range(1,number):
        fact = fact * i     #calculate factorial number
        i += 1
    print(f"{number} Factorial is : {fact}")   #display factorial number