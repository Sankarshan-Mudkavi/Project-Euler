"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

#Assuming the palindrome occurs with a multiple of 900+ and 900+
print max([mul1 * mul2 for mul1 in range(900,1000) for mul2 in range(900,1000) if str(mul1 * mul2) == str(mul1 * mul2)[::-1]])