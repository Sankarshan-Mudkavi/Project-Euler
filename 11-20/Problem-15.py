""" Starting in the top left corner of a 2x2 grid, and only being to the right and down, there are exactly 6 routes to the bottom corner. How many such routes exist in a 20x20 grid? """

def num_paths(grid_len, grid_height):
	num_paths = fact(grid_height + grid_len) / (fact(grid_len) * fact(grid_height))
	return num_paths

def fact(num):
	fact_res = 1
	for ind in range(num, 1, -1):
		fact_res *= ind
	return fact_res

print num_paths(20, 20)