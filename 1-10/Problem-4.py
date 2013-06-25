#Assuming the palindrome occurs with a multiple of 900+ and 900+
print max([mul1 * mul2 for mul1 in range(900,1000) for mul2 in range(900,1000) if str(mul1 * mul2) == str(mul1 * mul2)[::-1]])