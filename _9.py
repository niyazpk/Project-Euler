import math
import time

t1 = time.time()


def isqrt(n):
    c = n.bit_length()
    a, b = (c // 2, c % 2)  # divmod(n.bit_length(), 2)
    x = 2 ** (a + b)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


primes = [2, 3]
lenPrimes = 1
cut = 1

c3 = False

i = 5
while i < 2000000:
    prime = True
    sq = int(i ** 0.5)
    for p in primes:
        if i % p == 0:
            prime = False
            break
        if p > sq:
            break

    if prime:
        primes.append(i)

    c3 = not c3
    i += (2 if c3 else 4)

print sum(primes)
print time.time() - t1
