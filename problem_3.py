#!/usr/bin/python

'''
project_euler.net
problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

@see
https://en.wikipedia.org/wiki/Integer_factorization
'''

def solve_upwards(number):
    max = 1
    for i in xrange(2, number):
        if is_prime(i) and number % i == 0:
            max = i
        #print i
    return max

def solve_backwards(number):
    max = number
    for n in xrange(number, 1, -1):
        print n
    return max

def is_prime(number):
    i = 2
    while (i < number):
        if number % i == 0:
            return False
        i = i + 1
    return True

n = 600851475143
n = 147
print solve_upwards(n)
