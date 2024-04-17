#Write a Python program to returns sum of all divisors of a number

def divisors_list(number):      #create function
    divisors = []       #initialize list
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)  #add divisors number in a list
    return divisors

numbers = input("Enter a list of numbers separated by spaces : ").split()   #Input list of numbers separated by spaces

#Convert the input numbers to integers using a loop
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

#Iterate through the numbers, find divisors, and print them
for num in numbers:
    divisor_list = divisors_list(num)

print(f"Divisors number are : {divisor_list}") #display divisors number list

#Calculate the sum of divisors
for num in numbers:
    divisors = divisors_list(num)
    sum_of_divisors_result = sum(divisors)  #sum of all divisor number

print(f"Sum of divisors number : {sum_of_divisors_result}")     #display sum of all divisor number