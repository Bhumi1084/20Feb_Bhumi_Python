#Write a Python program to generate and print a list of first and last 5 elements where the values are square 
#of numbers between 1 and 30.

list1 = []  #initialize list

for i in range(1,31):
    list1.append(i*i)   #generate and square of number between 1 and 30

print("\n------First Five Element------")
print(list1[:5])    #display first five square element
print("\n------Last Five Element------")
print(list1[-5:],"\n")  #display last five square element