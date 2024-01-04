#-------------------------------------------------------------------------------
# Name:        exercises
# Purpose:
#
# Author:      omwira nk
#
# Created:     20/10/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Define a function that takes a tuple as an argument
def print_person_info(person):
    print("Name:", person[0], person[1])
    print("Age:", person[2])
    print("City:", person[3])

# Create a tuple with person information
person_info = ("John", "Doe", 30, "New York")

# Call the function and pass the tuple as an argument
print_person_info(person_info)
# In Python, you can indeed pass tuples as arguments to functions. Tuples are
# considered immutable data structures, which means they can be used as arguments to functions just like any other data type
# we define a function print_person_info that takes a single argument, which is a tuple containing information about a person. We then create a tuple person_info and pass it as an argument to the function. The function can access the elements of the tuple and print the person's name, age, and city.

# When you run the code, it will print the person's information correctly, demonstrating that you can pass tuples as function arguments in Python.