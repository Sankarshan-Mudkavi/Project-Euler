"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

#Basically just math
def sum_square(n):
    #We know that (1 + 2 + 3 + 4 + ... + n)^2 = (n * (n + 1) / 2)^2
    return (((n * (n + 1)) / 2) ** 2)

def squares_sum(n):
    #We know that (1^2 + 2^2 + 3^2 + ... + n^2 ) =  (n * (n + 1) * ((2 * n) + 1)) / 6
    return ((n * (n + 1) * ((2 * n) + 1)) / 6)

def ans(n):
    return sum_square(n) - squares_sum(n)

print ans(100)