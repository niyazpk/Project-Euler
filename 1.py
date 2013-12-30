#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
#-------------------------------------------



# Simple solution
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print (sum)


# Solution using arithmetic progression equations
sum = 0

for i in (3, 5):
    n = int(1000 / i)
    x = n * (n + 1) * i / 2
    sum += x

i = 15
n = int(999 / i)
x = n * (n + 1) * i / 2
sum -= x  #This was added twice in the for loop.

print(sum)
