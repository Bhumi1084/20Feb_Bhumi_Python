#Write a Python program to split a list into different variables.

list1 = []
n = int(input("Enter number of element : "))    #get value from user

if n!=0:
    for i in range(n):
        list1_input = input("Enter a number : ")    #get value from user
        list1.append(list1_input)   #add element in a list

    for j in range(n):
        print(f"var{j+1} = {list1[i]}")     #display list into different variable

else:
    print("Enter valid number of element.")



'''my_list = [10, 20, 30, 'B', 40]
var1, var2, var3, var4, var5 = my_list
print("var1 :", var1)
print("var2 :", var2)
print("var3 :", var3)
print("var4 :", var4)
print("var5 :", var5)'''