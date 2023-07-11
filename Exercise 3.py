#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#palindromstring : string = reversed of string

def if_palindrome(string):
   
    #the reversal becomes
       reverse= string[::-1]
       #indicating the length of the string
       for i in range(len(string)): 
           if string[i] != reverse[i]:
       #when the characters of each string doesn't match in like manner if reversed then the output 
           return False 
        #but if it matches then it should
           return True
       


# In[ ]:


#finding the third_most_frequent_letter in a string

def third_most_frequent_letter(l: str) -> str:
    # converting the string to lower-case using the lower() method.
    l = l.lower()
    
    
    # using a for loop, create a dictionary to count the occurance of each letter in the string.
    # We only count letters, ignoring any non-letter characters.
    number_of_letters= {}
    for characters in l:
        if characters.isalpha():
            if characters in number_of_letters:
                number_of_letters[characters] += 1
            else:
                number_of_letters[characters] = 1
    
    # sorting the dictionary by the occurance of each letter, in a descending order.
    number_of_letters_sorted = sorted(number_of_letters.items(), key=lambda x: x[1], reverse=True)
    
    # using the if and else function, outputing the third most frequent letter, 
    # or None if there are fewer than three letters in the string.
    
    if len(number_of_letters_sorted) >= 3:
        return number_of_letters_sorted[2][0]
    else:
        return None


# In[ ]:



   # Taking a string as a parameter and returning as a tuple
   
def counting(s: str) -> Tuple[int, int, int]:
   upper_case_letters = 0
   lower_case_letters = 0
   letter_count = 0
   
    #using a for loop to iterate over each character in the string with a isupper(), islower(), and isdigit() methods. 
   
   for t in s:
       if t.isupper():
           lower_case_letters += 1
       elif t.islower():
           lower_case_count += 1
       elif t.isdigit():
           letter_count += 1
   return (upper_case_letters, lower_case_letters, letter_count)

