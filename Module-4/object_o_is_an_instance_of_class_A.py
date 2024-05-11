# What is used to check whether an object o is an instance of class A?

class A:
    print("This is class A.")

o = A()   #Create object of class A

if isinstance(o, A):    #Check if obj is an instance of class A
    print("o is an instance of class A.")
else:
    print("o is not an instance of class A.")
