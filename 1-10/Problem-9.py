def py_trip(num):
	"""Since we know x + y > z, and x < z, and y < z, we conclude that x < (num / 2) - 1, and define y < x"""
	return [(x * y * (num - x - y)) for x in range(1, (num / 2) - 1) for y in range(1, x) if x ** 2 + y ** 2 == (num - x - y) ** 2]

print py_trip(1000)