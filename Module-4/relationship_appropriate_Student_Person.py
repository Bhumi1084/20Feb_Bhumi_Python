# What relationship is appropriate for Student and Person?

class Person:   #create class
    def setData(self, name):    #create method
        self.name = name
        print("Name:", self.name)   #display PersonName

class Student(Person):  #create class
    def setStudentID(self, student_id):     #create method
        self.student_id = student_id
        print("Student ID:", self.student_id)   #display student id

student = Student() #create object

name = input("Enter Student Name: ")    #get value from user
student_id = input("Enter Student ID: ")

student.setData(name)   #call function
student.setStudentID(student_id)
