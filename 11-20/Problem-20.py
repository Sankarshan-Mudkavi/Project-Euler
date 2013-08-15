"""n! eans n * (n - 1) * (n - 2) * ... 1
For example, 10! = 10 * 9 * 8 ... 2 * 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in 100!"""

print reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, range(1, 100)))])