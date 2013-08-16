def prime_gen(bound):
    primes = set([2])
    cur_prime = 3
    prime_list = [2]
    while len(prime_list) <= bound:
        isPrime = True
        for prime in primes:
            if cur_prime % prime == 0:
                isPrime = False
                cur_prime += 2
        if isPrime:
            primes.add(cur_prime)
            prime_list.append(cur_prime)
    return prime_list

print prime_gen(10000)[10000]