# Find the sum of the digits in the number 100!

p = 1
for i in range(1, 101):
    p *= i

s = 0
while(p):
    s += p % 10
    p /= 10

print s