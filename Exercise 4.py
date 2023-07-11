#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#function that takes the information of studens in a list of tuples and strings

def student_info(students, department):
    # generating a list of students in a department
    students_in_department = [(name, reg_num) for name, dept, reg_num in students if dept == department]

    # using an if function, generating an output message when there are no students in the department
    if not students_in_department:
        print("There seems to be no students in this department '{}'.".format(department))
        return

    # Sorting the students by their registration numbers
    students_in_department.sort(key=lambda student: student[1])

    # generating a table that indicates the information of the students
    print("Name\tReg_Number")
    print("----\t-------------------")
    for name, reg_num in students_in_department:
        print("{}\t{}".format(name, reg_num))


# In[ ]:


# using the input function, asking the user for the name of the file 
name_of_file = input("Please enter the name of the file: ")

try:
    # Opening the file and reading its lines into a list
    with open(name_of_file, "r") as f:
        lines = f.readlines()
except IOError:
    # generating an output error message if the file cannot be op
    print("Error: This file could not be opened.")
    exit()

# generating an empty list of tuples
Students = []

# splitting by commas on each line in the file and converting  to a tuple
# and adding it to the list of students
for line in lines:
    p = line.split(",")
    Student = (p[0], p[1], p[2])
    Students.append(Student)

# Print students lists
print("The List of students:")
print(Students)

# Looping until the user decides to quit
while True:
    # Asking the user for the department's name
    name_of_department = input("Enter your department's name: ")

    # Passing the user's input and list of students to a function 
    students_in_the_dept = take_students_in_the_dept(name_of_department, Students)

    # Print the list of students in the department
    print("Students in the department:")
    print(students_in_the_dept)

    # Now, asking if the user wants to quit
    answer = input("Do you want to quit now (y/n)? ")
    if answer.lower() == "y":
        break

