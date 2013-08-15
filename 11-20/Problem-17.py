""" If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage."""

single_digit = {0 : "", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
double_digit = {10 : "ten", 11 : "eleven", 12 : "twevle", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen"}
tens = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"}

def word_count():
	count = 0 #The total number of letters
	for num in range(0, 10):
		count += len(single_digit[num])
		print num, count
	for num in range(10, 20):
		count += len(double_digit[num])
		print num, count
	for num in range(20,1000):
		if len(str(num)) == 2:
			count += len(tens[int(str(num)[:1] + '0')]) + len(single_digit[num % 10])
		elif len(str(num)) == 3:
			count += len('hundredand') + len(single_digit[int(str(num)[:1])])
			if int(str(num)[1:2]) == 0:
				count += len(single_digit[int(str(num)[2:3])])
			elif int(str(num)[1:2]) == 1:
				count += len(double_digit[num % 100])
			else:
				count += len(tens[int(str(num)[1:2] + '0')]) + len(single_digit[int(str(num)[2:3])])
		print num, count
	return count + len('onethousand') - 27 #Removes length of extra 'and' after each hundred only value 

print word_count()