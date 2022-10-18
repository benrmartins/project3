import stdarray
import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Setup a 2D ragged list a of integers. The list must have n + 1 rows, with the ith (0 <= i
# <= n) row a[i] having i + 1 elements, each initialized to 1. For example, if n = 3, a should be
# initialized to [[1], [1, 1], [1, 1, 1], [1, 1, 1, 1]].
a = stdarray.create2D(n + 1, none)
for i in range(n + 1):
    a[i] = i + 1

# Fill the ragged list a using the formula for Pascal's triangle
#     a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
# where 0 <= i <= n and 1 <= j < i.
for i in range(0, i):
    for j in range(j, i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

# Write a to standard output.
for i in range(i, n):
    for j in range(j, n):
        if j != n:
            # If j is not the last column, write a[i][j] with a space after.
            a[i][j] = " "
        else:
            # Otherwise, write the element with a newline after.
            a[i][j] ="\n"
