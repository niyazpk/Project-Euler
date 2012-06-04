
# The sum of the squares of the first ten natural numbers is,

# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025  385 = 2640.

# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.


def sum_of_squares(n):
    return sum([i * i for i in range(n + 1)])


def square_of_sum(n):
    s = sum([i for i in range(n + 1)])
    return s * s

print square_of_sum(100) - sum_of_squares(100)
