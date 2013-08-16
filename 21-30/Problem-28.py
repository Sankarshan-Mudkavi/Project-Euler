"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

				21 22 23 24 25
				20  7  8  9 10
				19  6  1  2 11
				18  5  4  3 12
				17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

#Couldn't resist using list comprehensions
def spiral_gen(l_bound, h_bound): 
	return [(lengths, range(lengths**2, (lengths - 2)**2, -1)) for lengths in range(l_bound, h_bound + 1, 2)]

def diag_sum(l_bound, h_bound):
	spiral_list = spiral_gen(l_bound, h_bound)
	return 1 + reduce(lambda x, y : x + y, [sum([spi_list[1][0], spi_list[1][spi_list[0]-1], spi_list[1][spi_list[0]*2-2], spi_list[1][spi_list[0]*3-3]]) for spi_list in spiral_list])
		

print diag_sum(3, 1001)