"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""

#Very brute-force-ish

def abundant_nums():
	abundant_num_set = set()
	for num in range(12, 28123):
		if sum_div(num):
			abundant_num_set.add(num)
	return abundant_num_set

def sum_div(n):
	num_check = 0
	for ind in range(1, int(n/2)+1):
		if n % ind == 0:
			num_check += ind
	return num_check > n

def abundant_sum(set_of_abd_num):
	sum_abundant = 0
	for num in range(24, 28123):
		abd_num_sum = False
		for abd_num in range(num):
			if abd_num in set_of_abd_num and num - abd_num in set_of_abd_num:
				abd_num_sum = True
				break
		if not abd_num_sum:
			sum_abundant += num
	return sum_abundant

sets = abundant_nums()
print abundant_sum(sets) + sum(range(24))   