#This should be self explanatory
def fib(n):
	fib_list = []
	fib_list.append(1)
	fib_list.append(1)
	for i in range(2, n + 1):
		fib_list.append(fib_list[i - 1] + fib_list[i - 2])
	return fib_list[n]

def ans():
	sum_fib = 0
	n = 1
	while True:
		k = fib(n)
		if k > 4000000:
			break
		if k % 2 == 0:
			sum_fib += k
		n += 1
	return sum_fib

print ans()