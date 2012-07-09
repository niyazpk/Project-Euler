# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
#     which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and
# each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
# and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
# and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

n = 10000


from math import sqrt

a = range(2, 10000)
ln = len(a)
b = [1, 1] + [0, 1, 0, 1, 0, 0] * int(ln / 6)

for i in range(2, int(sqrt(ln))):
    for j in range(a[i] * a[i] - 2, b[i] * ln, 2 * a[i]):
        b[j] = 0

primes = [a[i] for i in range(ln) if b[i]]


# at this point we have a list of primes

sums = [0]

for i in range(1, n+1):
    sq = int(sqrt(i))
    factors = [j + i/j for j in range(2, sq + 1) if i%j == 0]
    sums.append(sum(factors) + 1)

s = 0

for k, v in enumerate(sums):
    if v < n and sums[v] == k and v != k:
        s += v

print s

