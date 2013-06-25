"""A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

def py_trip(num):
	#Since we know x + y > z, and x < z, and y < z, we conclude that x < (num / 2) - 1, and define y < x
	return [(x * y * (num - x - y)) for x in range(1, (num / 2) - 1) for y in range(1, x) if x ** 2 + y ** 2 == (num - x - y) ** 2]

print py_trip(1000)