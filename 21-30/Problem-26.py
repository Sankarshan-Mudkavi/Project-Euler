""" A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.It can be seen taht 1/7 has a 6 digit recurring cycle.
Find the value of d < 1000 for which 1/d has the longest recurring cycle in its decimal fraction part."""

def haupt_expt(a, n):
    isnotHaupt = True
    expt = 0
    while isnotHaupt:
        expt += 1
        if ((a**expt)-1) % n == 0:
            isnotHaupt = False
    return expt

def longest_seq(n):
    haupt_expt_var = 0
    longest = [0, 0]
    for num in range(1, n+1):
        new_num = extract_ten(num)
        haupt_expt_var = haupt_expt(10, new_num)
        if haupt_expt_var > longest[1]:
            longest = [num, haupt_expt_var]
    return longest

def extract_ten(num):
    if num == 2 or num == 5 or num == 4 or num == 8 or num == 10:
        num = 1
    else:
        while num % 2 == 0:
            num /= 2
        while num % 5 == 0:
            num /= 5
    return num

print longest_seq(1000)[0]

