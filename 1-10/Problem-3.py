"""def erato_sieve(n):
	num_list = [x for x in range(n)]
	comp_list = []
	for i in range(2,n):
		for j in range(2,n):
			k = i*j
			if k <= n:
				print k
				comp_list.append(k)
	return [x for x in num_list if x not in comp_list]

def erato_sieve(n):
    multiples = []
    for i in xrange(2, n+1):
        if i not in multiples:
            #print i
            for j in xrange(i*i, n+1, i):
                multiples.append(j)
    print 1
"""

import numpy
def primes_upto2(limit):
    is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
    for n in xrange(2, int(limit**0.5 + 1.5)): 
        if is_prime[n]:
            is_prime[n*n::n] = 0
    return numpy.nonzero(is_prime)[0][2:]

def div(n):
	div_list = []
	for i in range(1, n / 2):
		if n % i == 0:
			div_list.append(i)
	return div_list


def ans(n):
	fin_list = [x for x in div(n) if x in erato_sieve(n / 2)]
	return max(fin_list)

#print ans(60088)
print primes_upto2(600851475143)

