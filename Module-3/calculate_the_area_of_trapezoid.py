#Write a Python program to calculate the area of a trapezoid

length1 = float(input("Enter length of first base : "))     #get vale from user
length2 = float(input("Enter length of second base : "))
height = float(input("Enter the height of trapezoid : "))

area = (length1 + length2) * height / 2     #calculate the are of trapezoid
print("Area of a trapezoid : ",area)    #display area of a trapezoid