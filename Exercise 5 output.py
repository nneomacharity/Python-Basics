#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:


with open("C:\Users\DELL'\Downloads\Data File for Exercise 5.txt", 'r') as f:


# In[ ]:


num_students = int(f.readline())


# In[ ]:


inputs = np.array([[0, 0, 0, 0]] * num_students)
        inputs[i, 0] = reg_num
        inputs[i, 1] = exam
        inputs[i, 2] = coursework
        inputs[i, 3] = weighting


# In[ ]:


for i, line in enumerate(f):
        reg_num, exam, coursework, weighting = line.split()


# In[ ]:


data_of_student = np.array([(0, 0, 0, 0, '')] * num_students,
                         dtype=[('reg_num', int), ('exam', int), ('coursework', int), ('total', int), ('grade', 'U25')])


# In[ ]:


for i, row in enumerate(marks):
    reg_num, exam, coursework, weighting = row
    total = round(exam * weighting + coursework * (1 - weighting))
    
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


# In[ ]:


data_of_student[i] = (reg_num, exam, coursework, total, grade)
data_of_student = np.sort(student_data)


# In[ ]:




