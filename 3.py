#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#Simple solution
import math

def isPrime(num):
    if num % 2 ==0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

n = 600851475143

x = int(math.sqrt(n))

primeList = []

for i in range (3, x, 2):
    if isPrime(i) and (n % i == 0):
       primeList.append(i)
       if isPrime( n / i ):
          primeList.append( n / i )

for i in primeList:
    print(i)
