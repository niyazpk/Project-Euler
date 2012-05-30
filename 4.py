# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


# Brute force solution
s = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        x = str(i * j)
        l = len(x) / 2
        if x[:l] == x[l:][::-1] and x > s:
            s = x

print s

# elegant solution?


