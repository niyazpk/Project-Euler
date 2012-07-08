# Starting in the top left corner of a 22 grid,
# there are 6 routes (without backtracking) to the bottom right corner.


# How many routes are there through a 2020 grid?

f = 1
for i in range(1, 22):
    print i 
    f *= i

print f