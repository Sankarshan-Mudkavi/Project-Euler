from math import sqrt

def largest_prime_div(check_num):
    primes = set([2])
    cur_prime = 3
    prime_div = []
    while cur_prime < sqrt(check_num):
        isPrime = True
        for prime in primes:
            if cur_prime % prime == 0:
                isPrime = False
                cur_prime += 2
        if isPrime:
            primes.add(cur_prime)
            if check_num % cur_prime == 0:
                print cur_prime
                prime_div.append(cur_prime)
    return max(prime_div)
    
print largest_prime_div(600851475143)