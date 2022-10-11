import stdarray
import stdio
import sys

# Accept m (int) and n (int) as command-line arguments.
...

# Accept m x n floats from standard input and store them in a 2D list a.
a = ...
for i in range(...):
    for j in range(...):
        ...

# Set c (the transpose of a) to a 2D list with n rows and m columns, with all the elements
# initialized to 0.0
...

# Fill in the elements of c such that c[i][j] = a[j][i], where 0 <= i < n and 0 <= j < m.
for i in range(...):
    for j in range(...):
        ...

# Write c to standard output.
for i in range(...):
    for j in range(...):
        if ...:
            # If j is not the last column, write c[i][j] with a space after.
            ...
        else:
            # Otherwise, write the element with a newline after.
            ...
