def num_gen(n):
	return n*(n+1)/2

def num_div(num):
	count = 0
	for i in range(int(num/2)+1):
		if num % (i+1) == 0:
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