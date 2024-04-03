#Write a Python function that takes a list and returns a new list with unique elements of the first list.

def printUniqueElement(input_element):  # Function to print unique elements
    unique_elements = set(input_element)  # Convert input list to a set to remove duplicates
    print(list(unique_elements))  # Print unique elements as a list

list1 = []  # Initialize list
n = int(input("Enter the number of elements: "))  # Get the number of elements from the user
for i in range(n):
    input_element = input("Enter an element: ")
    list1.append(input_element)  # Append elements to the list

printUniqueElement(list1)  # Call function to print unique elements
