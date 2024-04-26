#Write a Python function to check whether a number is perfect or not.

def perfect_number(n):      #create function
    sum = 0     #initialize
    for i in range(1, n):
        if n % i == 0:  
            sum += i    #sum of divisior number
    if sum == n:    #check sum equal to number
        print("Number Is Perfect.")
    else:
        print("Number Is Not Perfect.")
    #return sum == n

user_input = int(input("Enter Number : "))      #get value from user
print(perfect_number(user_input))   #call function