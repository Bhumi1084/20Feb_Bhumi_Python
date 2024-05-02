# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

'''

=> First try clause is executed i.e. the code between try and except clause.
=> If there is no exception, then only try clause will run, except clause will not get executed.
=> If any exception occurs, the try clause will be skipped and except clause will run.
=> A try statement can have more than one except clause.
=> Finally block always gets executed either exception is generated or not

'''

#Example : 

def calculate(x, y):
    try:
        sum = x + y     #calculate addition
        div = x / y     #calculate division
        mult = x * y    #calculate multiplication
        sub = x - y     #calculate subtraction
        print("Addition : ",sum)    #Display sum
        print("Division : ",div)    #Display div
        print("Multiplication : ",mult)     #Display mult
        print("Subtraction : ",sub)     #Display sub
    except Exception as e:
        print(e)    #Handling and Display error
    finally:    #this block always executed
        print("This is always executed")    #display message
        
x = int(input("Enter first number : "))     #get value from user
y = int(input("Enter second number :"))
calculate(x, y)     #call function