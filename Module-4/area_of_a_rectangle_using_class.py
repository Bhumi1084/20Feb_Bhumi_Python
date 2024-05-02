#Write a Python class named Rectangle constructed by a length and width and a method which will compute the 
#area of a rectangle

class Rectangle:    #create class
    def getData(self, length, width):   #create function
        self.length = length    
        self.width = width
        
    def calculate_area(self):   #create function
        self.area = self.length * self.width    #calculate area of rectangle
        
rectangle = Rectangle() #create object

length = int(input("Enter length : "))  #get value from user
width = int(input("Enter width : "))

rectangle.getData(length, width)    #call function
rectangle.calculate_area()  #call function
print("Area of the rectangle : ",rectangle.area)    #Display message