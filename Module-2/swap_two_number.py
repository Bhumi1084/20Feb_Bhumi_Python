#Write python program that swap two number with temp variable and without temp variable.


first_number = int(input("Enter First Number : "))      #get value from user
second_number = int(input("Enter Second Number : "))    #get value from user

#swap two number with temp variable
#logic for swap number with thired variable
temp = first_number     
first_number = second_number
second_number = temp

print("---------After swapping value---------")
print(f"First Number : {first_number} \nSecond Number : {second_number}")       #print after swapping value

#swap two number without temp variable
#logic for swap number without thired variable
first_number = first_number + second_number
second_number = first_number - second_number
first_number = first_number - second_number

print("---------After swapping value---------")
print(f"First Number : {first_number} \nSecond Number : {second_number}")   #print after swapping value