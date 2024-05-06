# Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python?

'''

Inheritance in Python :

-> Inheritance is defined as the mechanism of inheriting the properties of the base class to the child class.
=> There are main three types of inheritance in Python:
1. Single Inheritance : Single inheritance enables a derived class to inherit properties from a single parent class it's called single level inheritance.
2. Multiple Inheritance : When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
3. Multilevel Inheritance : In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. This is similar to a relationship representing a child and a grandfather. 
4. Hierarchical Inheritance : When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance. In this program, we have a parent class and two child classes.

What is init? Or What Is A Constructor In Python? :

-> In Python, a constructor is a special method that is called when an object is created.
-> The purpose of a python constructor is to assign values to the data members within the class when an object is initialized.
-> The name of the constructor method is always __init__.

'''

#Example :

class StudInfo:     #create class
    def __init__(self, id, name, subject): 
        self.id = id
        self.name = name
        self.subject = subject

class StudData(StudInfo):  #create and inherite class
    def studData(self):     #create function
        print("Id : ",self.id)      #display id
        print("Name : ",self.name)      #display name
        print("Subject : ",self.subject)    #display subject

id = int(input("Enter Student id : "))
name = input("Enter Student Name : ")
subject = input("Enter Student Subject : ")

stud = StudData(id, name, subject)   #Creating instances of subclasses
stud.studData()