"""The Fibonacci sequence is defined by the recurrence relation: f_{n} = f_{n - 1} + f_{n - 2}, where f_{1} and f_{2} = 1.

Hence the first twevle terms will be: f_{1} = 1, f_{2} = 1, f_{3} = 2, f_{4} = 3, f_{5} = 5, f_{6} = 8, f_{7} = 13, f_{8} = 21, f_{9} = 34, f_{10} = 55, f_{11} = 89, f_{12} = 144.

The 12th term, f_{12} is the first term to contain three digits. What is the first term in the Fibonacci sequence to contain 1000 digits?"""

def fibo(num, fibo_dict):
	if num not in fibo_dict:
		fibo_dict[num] = fibo(num - 1, fibo_dict) + fibo(num - 2, fibo_dict)
	return fibo_dict[num]


def fibo_ans():
	not_thousand = True
	index = 2
	fibo_dict = {1 : 1, 2 : 1}
	while not_thousand:
		index += 1
		if len(str(fibo(index, fibo_dict))) >= 1000:
			not_thousand = False
	return index

print fibo_ans()
