# How to Define a Class in Python? What Is Self? Give An Example Of A Python Class

'''

=> A class is a user-defined blueprint or prototype from which objects are created.
=> Self represents the instance of the class.
=> By using the “self”  we can access the attributes and methods of the class in Python.
=> It is customary to use “self” as the first parameter in instance methods of a class.
=> Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter.

'''

#Example : 

class Car:  #create class
    
    def __init__(self, id, name, age):  #Constructor method
        self.id = id
        self.name = name
        self.age = age
        
    def display_info(self):     #create function
        print(f"Id : {self.id}\nName : {self.name}\nAge : {self.age}")      #display value
        
id = int(input("Enter Your Id : "))     #get value from user
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

carObj = Car(id,name,age)   #create object
carObj.display_info()   #call function