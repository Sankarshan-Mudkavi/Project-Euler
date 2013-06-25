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
    return prime_div

print largest_prime_div(37)