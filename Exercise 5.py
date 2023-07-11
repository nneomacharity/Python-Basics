#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# Open the file for reading
with open('marks.txt', 'r') as f:
    # Reading the first line to get the number of students
    num_students = int(f.readline())

    # Creating a  2 dimensional NumPy array with the appropriate number of rows and 4 columns
    inputs = np.array([[0, 0, 0, 0]] * num_students)

    # Iterating over the remaining lines in the file
    for i, line in enumerate(f):
        # Split the line by whitespace to get the marks for the student
        reg_num, exam, coursework, weighting = line.split()

         # Storing the inputs in the appropriate row of the array
        inputs[i, 0] = reg_num
        inputs[i, 1] = exam
        inputs[i, 2] = coursework
        inputs[i, 3] = weighting


# Creating a structured NumPy array with the appropriate fields
data_of_student = np.array([(0, 0, 0, 0, '')] * num_students,
                         dtype=[('reg_num', int), ('exam', int), ('coursework', int), ('total', int), ('grade', 'U25')])

# Iterate over the rows in the marks array
for i, row in enumerate(marks):
    # Extracting the marks for each student
    reg_num, exam, coursework, weighting = row

    # Calculating the total mark using the exam, coursework, and weighting
    total = round(exam * weighting + coursework * (1 - weighting))

    # Determine the grade for the student
    if total >= 70:
        grade = 'First'
    elif total >= 60:
        grade = 'Second_Upper'
    elif total >= 50:
        grade = 'Second_Lower'
    elif total >= 40:
        grade = 'Third'
    else:
        grade = 'Fail'

    # Storing the calculated values in the structured array
    data_of_student[i] = (reg_num, exam, coursework, total, grade)

# Sort the structured array by total mark
data_of_student = np.sort(student_data)

