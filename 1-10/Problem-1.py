""" If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000. """

def num_gen(n):
	return n*(n+1)/2

def num_div(num):
	count = 0
	for i in range(int(num/2)+1):
		if num % (i+1) == 0
			count += 1
	return count

def over_fhund():
	boo = 1
	i = 1
	while boo == 1:
		k = num_gen(i)
		if num_div(k) > 500:
			boo = 0
		i = i + 1
	return i-1

print over_fhund()
