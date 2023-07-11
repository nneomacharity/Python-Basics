#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# A function that takes list of the prime numbers between two positive integers supplied as arguments.
# defining a variable that indicates the expected range for the function and required outputs using a for loop and an if function
# carrying out the program using the input function

def prime_num(i, j):
    prime_fig =[]
    for figures in range (i, j+1):
        it_is_prime = True
       # where i and j indicates the first and last values of the expected range
        
        
# indicating what happens if the number isn't prime
        for divisor in range(2, figures):
            if figures % divisor == 0:
                it_is_prime = False
                break

        # however, if the resulting inputs are in prime numbers, then it should be appended
        if it_is_prime:
            prime_fig.append(figures)

    return prime_fig

i = input('Please enter the first value of your range:')
j = input('Please enter the last value of your range:')

# indicating corresponding outputs if inputs are not of integer data types or they are less than zero
try:
    i = int(i)
    j = int(j)
except ValueError:
    print("Incorrect input: Try again making sure that your first and last values are positive integers.")
    exit()

if i < 0 or j < 0:
    print("Incorrect input: Try again making sure that your first and last values are greater than zero.")
    exit()
    
if i > j:
    i, j= j, i

# The entire list of expected prime values becomes
prime_fig = prime_num(i, j)

# printing theses values with up to 10 on each line
for k, prime in enumerate(prime_fig):
    print(prime, end =" ")
    if (k + 1) % 10 == 0:
        print()


# In[ ]:



def get_primes(start, end):
    primes = []

    for num in range(start, end+1):
        is_prime = True

        # check if the number is prime
        for divisor in range(2, num):
            if num % divisor == 0:
                is_prime = False
                break

        # if the number is prime, append it to the list
        if is_prime:
            primes.append(num)

    return primes

# main program
start = input("Enter the start of the range: ")
end = input("Enter the end of the range: ")

# make sure the input is valid
try:
    start = int(start)
    end = int(end)
except ValueError:
    print("Invalid input. Both numbers must be positive integers.")
    exit()

if start < 0 or end < 0:
    print("Invalid input. Both numbers must be positive integers.")
    exit()

# ensure that start <= end
if start > end:
    start, end = end, start

# get the list of prime numbers
primes = get_primes(start, end)

# print the numbers, 10 per line
for i, prime in enumerate(primes):
    print(prime, end=" ")
    if (k + 1) % 10 == 0:
        print()


# In[ ]:




