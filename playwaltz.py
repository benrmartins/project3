import stdaudio
import stdio
import sys

# stored the numbers the file into a variable
waltz = stdio.readAllInts()

# exited if the measure is not 32
if len(waltz) != 32:
    sys.exit("A waltz must contain exactly 32 measures")

# looped through the first 16 minutes
for min in waltz[0:16]:
    # exited if the number was greater 176 and less than 1
    if min > 176 or min < 1:
        sys.exit("A minuet measure must be from [1, 176]")

# checked if the number was in the first 16 min
if min in waltz[1:16]:
    # stored the filename along with the number of the sound
    filename = "data/M" + str(min)
    # played the sound using from the file name
    stdaudio.playFile(filename)

# looped through the last 16 minutes
for trio in waltz[16:32]:
    # exited if the number was greater 96 and less than 1
    if trio > 96 or trio < 1:
        sys.exit("A trio measure must be from [1, 96]")

# checked if the number was in the last 16 min
if trio in waltz[16:32]:
    # stored the filename along with the number of the sound
    filename = "data/T" + str(trio)
    # played the sound using from the file name
    stdaudio.playFile(filename)
