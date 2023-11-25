line = [
    'R:Teddy| 4 18:12 - 6 19:32, 17 13:12 - 20 14:42',
    'R:Dolores| 12 14:12 - 12 18:15',
    'R:Mave| 13 9:21 - 13 21:23, 14 7:23 - 15 12:12 , 17 18:00 - 19 23:22, 22 20:25 - 26 15:14 ',
    'R:Peter| 8 9:05 - 10 4:55',
    'R:Clementine| 15 4:00 - 16 14:43',
    'T:8 14:21',
    'T:17 19:17'
]

robots = {}

def parseTime(dayTime):
    day, timeH, timeM = list(map(int, dayTime.replace(':', ' ').split(" ")))
    print(dayTime, day, timeH, timeM)
    return (day - 1) * 1440 + timeH * 60 + timeM


def parsePeriod(periodLine):
    pseudoTimestampPeriods = []
    rPeriods = periodLine.strip().split(", ")
    for rP in rPeriods:
        pseudoTimestampPeriods = list(map(parseTime, rP.split(" - ")))
    return pseudoTimestampPeriods


def parseRobot(info):
    rName, rPeriods = info.split("|")
    rPeriods = parsePeriod(rPeriods)
    print("ROBOT", rName, rPeriods)


def parseLine(info):
    if info.startswith('R:'):
        parseRobot(info.replace("R:", ""))
    elif info.startswith('T:'):
        print("TIME")


for l in line:
    parseLine(l)