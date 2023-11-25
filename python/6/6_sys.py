import sys

robots = {}

def parseTime(dayTime):
    day, timeH, timeM = list(map(int, dayTime.strip().replace(':', ' ').split(" ")))
    # print(dayTime, day, timeH, timeM)
    return (day - 1) * 1440 + timeH * 60 + timeM


def parsePeriod(periodLine):
    pseudoTimestampPeriods = []
    rPeriods = periodLine.strip().split(", ")
    for rP in rPeriods:
        pseudoTimestampPeriods.append(list(map(parseTime, rP.split(" - "))))
    return pseudoTimestampPeriods


def parseRobot(info):
    rName, rPeriods = info.split("|")
    robots[rName] = parsePeriod(rPeriods)
    # print("ROBOT", rName, rPeriods)


def checkRobots(time):
    # print("TIME", parseTime(time))
    print(time)
    time = parseTime(time)
    for robotName, robotTimePeriods in robots.items():
        gameOver = False
        for timeP in robotTimePeriods:
            if (timeP[0] <= time <= timeP[1]):
                gameOver = True
                break
        print(robotName + " " + ("GAME OVER" if gameOver else "GAME CONTINUES"))


def parseLine(info):
    if info.startswith('R:'):
        parseRobot(info.replace("R:", ""))
    elif info.startswith('T:'):
        checkRobots(info.replace("T:", ""))


for line in sys.stdin:
    # print(line.strip())
    parseLine(line.strip())