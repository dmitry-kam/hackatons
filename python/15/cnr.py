import sys

def parseLine(line):
    global nonogramLines, nonogramRows, modeInsert
    line = line.strip()
    if len(line) == 0:
        modeInsert = 1
    else:
        figures = list(map(int, line.split(',')))
        if modeInsert == 1:
            nonogramLines.append(figures)
        else:
            nonogramRows.append(figures)


for line in sys.stdin:
    parseLine(line)

nonogramLinesOrig, nonogramRowsOrig = list(nonogramLines), list(nonogramRows)
height, width = len(nonogramLines), len(nonogramRows)