#When will the else part of try-except-else be executed?

'''

=> An Exception is an Unexpected Event, which occurs during the execution of the program.
=> It is also known as a run time error.
=> When that error occurs, Python generates an exception during the execution and that can be handled, 
    which prevents your program from interrupting. 
=> Try: This block will test the excepted error to occur
=> Except:  Here you can handle the error
=> Else: If there is no exception then this block will be executed
    
'''

#Example :
try:
    a=int(input("Enter value of A:"))   #get value from user
    b=int(input("Enter value of B:"))
    print("Sum:",a+b)   #display sum
except:
    print("Error!")
else:
    print("This is finally block!")