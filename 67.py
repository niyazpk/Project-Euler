# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom in 67.txt, a 15K text file
# containing a triangle with one-hundred rows.



t = open('67.txt').read().split('\n')
a = map(lambda x: x.split(' '), t)

a = [map(int, x) for x in a]

for i in range(len(a) -2, -1, -1):
    for j, v in enumerate(a[i]):
        a[i][j] =  v + max(a[i+1][j], a[i+1][j+1])

print a[0][0]