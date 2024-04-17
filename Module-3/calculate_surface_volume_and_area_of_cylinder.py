#Write a Python program to calculate surface volume and area of a cylinder.

radius = float(input("Enter the radius of the cylinder: "))     #get value from user
height = float(input("Enter the height of the cylinder: "))
pi = 3.24 

surface_area = 2 * pi * radius * (radius + height)  #Calculate the surface area of the cylinder

volume = pi * radius ** 2 * height  #Calculate the volume of the cylinder

print("Surface Area of the cylinder : ", surface_area)    #display surface area
print("Volume of the cylinder : ", volume)      #display volume of a cylinder