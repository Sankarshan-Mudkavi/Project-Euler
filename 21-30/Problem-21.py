"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000."""

def sum_div(num):
	div_sum = 0

	#One-liner: return reduce(lambda x, y: x + y, [facts for facts in range(1, int(num/2) + 1) if num % facts == 0], 0)
	
	for facts in range(1, int(num/2) + 1):
		if num % facts == 0:
			div_sum += facts
	return div_sum

def num_dict_gen(bound):
	factsum_dict = {}
	for num in range(1, bound):
		factsum_dict[num] = sum_div(num)
	return factsum_dict

def amic_pairs(bound):
	amic_numset = set()
	factsum_dict = num_dict_gen(bound)

	#Using set comprehensions: return sum({keys for keys in factsum_dict if sum_div(factsum_dict[keys]) == keys and keys != factsum_dict[keys]})
	
	for keys in factsum_dict:
		if sum_div(factsum_dict[keys]) == keys and keys != factsum_dict[keys]:
			amic_numset.add(keys)
	return sum(amic_numset)

print amic_pairs(10000)