# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:18:34 2022

@author: Roger Hegstrom (rhegstrom@avc.edu)

A prime number is a number whose only divisors are 1 and itself.  
For example 1, 2, 3 5, 7, 11, 13 .. are prime numbers, but 9 (divisor of 3),  51 (divisor of 3) .. are not prime.
Write a python program to print out all the prime numbers < 1000

Here's a link to my github account link Links to an external site.

Fork this to your GitHub account, or alternately simply open your own repository, write code to get the prime numbers and push the code to your account, and turn in the URL
"""

def isPrime(num):
    if num % 2 == 0:  # skip even numbers
        return False
    
    for i in range(2,num):
        if num % i == 0: 
            return False
    
    return True


primes = [i for i in range(1, 1001) if isPrime(i) == True]

print(primes)




