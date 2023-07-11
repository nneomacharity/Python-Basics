#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#program that asks the user to input his/her date of birth

import datetime 
from datetime import date


#defining a variable to calculate the age as an integer
def age_calculator(born: datetime.date) -> int:
    present_day = datetime.date.today()
    users_age = present_day.year -born.year
    if (present_day.month, present_day.day)< (born.month, born.day):
        users_age -=1
        return users_age
    
# Generating  another variable to determine input pattern for the user and follow up error information if inputed wrongly

def valid_date(date_string: str) -> datetime.date:
    try:
        return datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    except Error_in_date:
        raise Error_in_date(f"Invalid form of input, try again following the pattern  indicated: {date_string}")
        
# using the input function, calling out the required output
def user_birthday():
    birth_date= input("Hello, kindly enter your date of birth in this format dd/mm/yyyy: ")
    birthday = parse_date(birth_date)
    actual_age = age_calculator(birthday)
    print(f"Thanks for yor response, you are {actual_age} years old.")
    
if birthday.month == datetime.date.present_day().month and birthday.day == datetime.date.present_day().day:
    print("Happy birthday to you!")
    
if__name__ == "__birth_date__"
birth_date()

