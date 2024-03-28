#Write a Python function to get the largest number, smallest num and sum of all from a list.

def get_stats(numbers):     #create function
    #if not numbers:
        #return None, None, 0
    
    max_num = max(numbers)      #find max value
    min_num = min(numbers)      #find min value
    total_sum = 0   #initialize 
    for num in numbers:
        total_sum += num       #calculate total sum
    
    return max_num, min_num, total_sum

list1 = []  #create list
n = int(input("Enter number of element : "))    #get a value from user

for i in range(n):
    element = int(input("Enter a element : "))  
    list1.append(element)   #add a element in the list

largest, smallest, total_sum = get_stats(list1)
print("\nLargest Number : ",largest)    #display largest value
print("Smallest Number : ",smallest)    #display smallest value
print("Total sum : ",total_sum)     #display total sum