import stdaudio
import stdio
import sys

waltzMeasure = stdio.readAllInts()

if len(waltzMeasure) != 32:
    sys.exit()
for minuetMeasure in waltzMeasure[0, 16]:
    if(minuetMeasure <= 1 or minuetMeasure >= 76):
        sys.exit()

# same

for minuetMeasure in waltzMeasure[0, 16]:
    fileName = 'data/M' + str(minuetMeasure)
    stdaudio.playFile(fileName);

# 16-32
