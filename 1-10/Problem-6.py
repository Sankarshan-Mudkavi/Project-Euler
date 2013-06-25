#Basically just math
def sum_square(n):
    """ We know that (1 + 2 + 3 + 4 + ... + n)^2 = (n * (n + 1) / 2)^2 """
    return (((n * (n + 1)) / 2) ** 2)

def squares_sum(n):
    """ We know that (1^2 + 2^2 + 3^2 + ... + n^2 ) =  (n * (n + 1) * ((2 * n) + 1)) / 6 """
    return ((n * (n + 1) * ((2 * n) + 1)) / 6)

def ans(n):
    return sum_square(n) - squares_sum(n)

print ans(100)