#Write a Python function to check whether a number is in a given range

def is_in_range(number, start, end):    #create function
    if number >= start and number <= end:
        print(f"The number {number} is in the given range [{start}, {end}].")
    else:
        print(f"The number {number} is not in the given range [{start}, {end}].")

number = int(input("Enter a number : "))    #get value from user
range_start = int(input("Enter the start of the range : "))
range_end = int(input("Enter the end of the range : "))

is_in_range(number, range_start, range_end)     #call function