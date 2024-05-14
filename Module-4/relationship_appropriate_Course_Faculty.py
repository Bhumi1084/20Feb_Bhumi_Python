# What relationship is appropriate for Course and Faculty?

class Faculty:  #create class
    def getData(self, faculty_name):    #create method
        self.faculty_name = faculty_name
        print("Faculty Name:", self.faculty_name)   #display faculty name

class Course(Faculty):
    def getCourse(self, course_name):   #create method
        self.course_name = course_name
        print("Course Name:", self.course_name)     #display course name

c1 = Course()   #create object

fname = input("Enter Faculty Name : ")      #get value from user
cname = input("Enter Course Name : ")

c1.getData(fname)   #call method
c1.getCourse(cname)