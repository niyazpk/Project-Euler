# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# Brute force solution
s = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        x = i * j
        if str(x) == str(x)[::-1] and x > s:
            s = x
            c = [i, j]

print s, c

# faster solution?

