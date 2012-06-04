# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?


# (This answer is a mofification of the answer for Q.9)

import time
from math import sqrt

t1 = time.time()


a = range(2, 2000000)
ln = len(a)
b = [1, 1] + [0, 1, 0, 1, 0, 0] * int(ln / 6)

for i in range(2, int(sqrt(ln))):
    for j in range(a[i] * a[i] - 2, b[i] * ln, 2 * a[i]):
        b[j] = 0

print [a[i] for i in range(ln) if b[i]][10001 - 1]
print time.time() - t1








