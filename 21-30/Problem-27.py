"""Euler discovered the remarkable quadratic formula: n^2 + n + 41.

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.

 However, when n = 40, 40^2 + 40 + 41 is divisble by 41 and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

 The incredible formula n^2 -79n + 1601 was discovered which produces 80 primes for the first 80 consecutive values of n = 0 to n = 79. The product of the coeffecients , -79 and 1601 is -126479.

Considering quadratics of the form: n^2 + an + b, where abs(a) < 1000 and abs(b) < 1000.

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0."""

#I'm surprised the brute force worked, and with such quick execution times too.

def quad_primes():
	longest_chain = [0, 0, 0]
	for a_coeff in range(-1000, 1001):
		for b_coeff in range(-1000, 1001):
			still_prime = True
			count = -1
			num_primes = -1
			while still_prime:
				count += 1
				num_primes += 1
				if not is_prime(count, a_coeff, b_coeff):
					still_prime = False
					if num_primes > longest_chain[0]:
						longest_chain[0] = num_primes
						longest_chain[1] = a_coeff
						longest_chain[2] = b_coeff
	return longest_chain[1]*longest_chain[2]

def is_prime(num, a_coeff, b_coeff):
	prime_check = abs(num**2 + a_coeff*num + b_coeff)
	prime_count = 0
	for count in range(1, int(prime_check / 2) + 1):
		if prime_check % count == 0:
			prime_count += 1
			if prime_count > 1:
				return False
	return True 

print quad_primes()