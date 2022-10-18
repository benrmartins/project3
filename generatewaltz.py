import stdarray
import stdrandom
import stdio

minuetMeasure = stdarray.create2D(11, 16, 0)
trioMeasure = stdarray.create2D(6, 16, 0)

for i in range(11):
    for j in range(16):
        minuetMeasure[i][j] = stdarray.readInt()
        i = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7)
        minuetMeasure = minuetMeasure[i][j]
        stdio.writeln(str(minuetMeasure) + " ")

for i in range(6):
    for j in range(16):
        trioMeasure[i][j] = stdarray.readInt()
        i = stdrandom.uniformInt(1, 7) + stdrandom.uniformInt(1, 7)
        trioMeasure = trioMeasure[i][j]
        stdio.writeln(str(trioMeasure) + " ")







