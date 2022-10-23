from typing import Any

import stdarray
import stdrandom
import stdio

# Created a 2 2 D arrays, 11 by 16 and 6 by 16 with 0s inside it
minMeasure = stdarray.create2D(11, 16, 0)

trio = stdarray.create2D(6, 16, 0)

# looped through the 11 by 16 array
for i in range(11):
    for j in range(16):
        # replaced each 0 in the 2d array to a number in the file
        minMeasure[i][j] = stdio.readInt()

# looped through the columns of the array of numbers
for j in range(16):
    # randomly from a roll, chose a two rows from the array of numbers and added them together
    i = (stdrandom.uniformInt(1, 7) - 1) + (stdrandom.uniformInt(1, 7) - 1)
    # stored the exact value of the row and column into a variable
    minsMeasure = minMeasure[i][j]
    # displayed the numbers onto the terminal
    stdio.write(str(minsMeasure) + " ")

# looped through the 6 by 16 array
for i in range(6):
    for j in range(16):
        # replaced each 0 in the 2d array to a number in the file
        trio[i][j] = stdio.readInt()

# looped through the columns of the array of numbers
for j in range(16):
    # randomly from a roll, chose a row from the array of numbers
    i = stdrandom.uniformInt(1, 7) - 1
    # stored the exact value of the row and column into a variable
    trios = trio[i][j]
    # displayed the numbers onto the terminal
    stdio.write(str(trios) + " ")

stdio.writeln()
