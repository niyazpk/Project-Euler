# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import time
from math import sqrt

t1 = time.time()


a = range(2, 2000000)
ln = len(a)
b = [1, 1] + [0, 1, 0, 1, 0, 0] * int(ln / 6)

for i in range(2, int(sqrt(ln))):
    for j in range(a[i] * a[i] - 2, b[i] * ln, 2 * a[i]):
        b[j] = 0

print sum(a[i] for i in range(ln) if b[i])
print time.time() - t1
