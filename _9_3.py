from math import sqrt
import time

t1 = time.time()


def sieveOfErat(end):
    if end < 2:
        return []

    #The array doesn't need to include even numbers
    lng = ((end / 2) - 1 + end % 2)

    # Create array and assume all numbers in array are prime
    sieve = [True] * (lng + 1)

    # In the following code, you're going to see some funky
    # bit shifting and stuff, this is just transforming i and j
    # so that they represent the proper elements in the array.
    # The transforming is not optimal, and the number of
    # operations involved can be reduced.

    # Only go up to square root of the end
    for i in range(int(sqrt(end)) >> 1):

        # Skip numbers that aren't marked as prime
        #if not sieve[i]:
        #    continue

        # Unmark all multiples of i, starting at i**2
        for j in range((i * (i + 3) << 1) + 3, sieve[i] * lng, (i << 1) + 3):
            sieve[j] = False

    # Don't forget 2!
    primes = [2]

    # Gather all the primes into a list, leaving out the composite numbers
    primes.extend([(i << 1) + 3 for i in range(lng) if sieve[i]])

    return primes


print sum(sieveOfErat(2000000))

print time.time() - t1
