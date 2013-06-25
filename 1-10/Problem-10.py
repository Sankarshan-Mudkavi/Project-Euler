#Using the method for Problem 7 was taking far too long, so I used a sieve.
def prime_sum(n):
    primed = [0] * n
    cur_prime = 3
    prime_sum = 2
    while cur_prime < n:
        if primed[cur_prime] == 0:
            prime_sum += cur_prime
            multiples = cur_prime
            while multiples < n:
                primed[multiples] = 1
                multiples += cur_prime
        cur_prime += 2
    return prime_sum

print prime_sum(2000000)