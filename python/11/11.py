import sys

mineField = []
doloresCoord = {}
williamCoord = {}

def doStep(coords):
    if coords['action'] == 'up':
        return {'x': coords['x'], 'y': coords['y'] - 1}
    elif coords['action'] == 'down':
        return {'x': coords['x'], 'y': coords['y'] + 1}
    elif coords['action'] == 'left':
        return {'x': coords['x'] - 1, 'y': coords['y']}
    elif coords['action'] == 'right':
        return {'x': coords['x'] + 1, 'y': coords['y']}


def isInjured():
    global doloresCoord, williamCoord, mineField
    [doloresCoord, williamCoord] = list(map(doStep, [doloresCoord, williamCoord]))
    shift, sumC, lenMines = williamCoord['y'] - williamCoord['x'], williamCoord['y'] + williamCoord['x'], len(mineField)
    diagA = [{'x': x, 'y': x + shift} for x in range(lenMines)]
    diagB = [{'x': x, 'y': -x + sumC} for x in range(lenMines)]
    if doloresCoord in diagA or doloresCoord in diagB:
        print("Yes")
    else:
        print("No")


def parseLine(line):
    global doloresCoord, williamCoord
    if line.startswith(('X', '0', 'D', 'W')):
        mineField.append(list(line))
        if "W" in line:
            williamCoord = {'x': line.index("W"), 'y': len(mineField) - 1}
        if "D" in line:
            doloresCoord = {'x': line.index("D"), 'y': len(mineField) - 1}
    elif line.startswith(('up', 'down', 'left', 'right')):
        if 'action' not in doloresCoord:
            doloresCoord['action'] = line
        else:
            williamCoord['action'] = line
            isInjured()


for line in sys.stdin:
    parseLine(line.strip())