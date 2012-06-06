# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Solution uses Euclid's formula:
# http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

# a = m ** 2 - n ** 2
# b = 2 * m * n
# c = m ** 2 + n ** 2

for i in range(1, 501):
    if not 500 % i:
        x = i
        y = 500 / i

        if y > x:
            x, y = y, x

        m = y
        n = x - y

        if n > m:
            m, n = n, m

        a = (m * m) - (n * n)
        b = 2 * m * n
        c = m * m + n * n

        if a + b + c == 1000:
            print a * b * c
            break
