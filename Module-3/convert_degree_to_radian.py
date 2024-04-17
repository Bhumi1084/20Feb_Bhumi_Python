#Write a Python program to convert degree to radian

def degress_to_radian(degrees):     #create function
    pi = 3.14
    radians = degrees * (pi/180)    #calculate degree to radian
    print("degree to radians : ", radians)  #display radians

d1 = float(input("Enter the degree : "))    #get value from user
degress_to_radian(d1)   #call function