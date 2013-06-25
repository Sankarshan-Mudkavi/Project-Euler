""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143? """

from math import sqrt

def largest_prime_div(check_num):
    primes = set([])
    cur_prime = 2
    prime_div = []
    while cur_prime < check_num:
        isPrime = True
        for prime in primes:
            if cur_prime % prime == 0:
                isPrime = False
                cur_prime += 1
        if isPrime:
            primes.add(cur_prime)
            if check_num % cur_prime == 0:
                prime_div.append(cur_prime)
    return max(prime_div)

print largest_prime_div(600851475143)