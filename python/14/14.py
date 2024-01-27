import math
import sys

days = 0   # n - days
investors = 0   # k - investors
inputArray = []

def parseLine(line):
    global days,investors,inputArray
    if len(line) == 1:
        if (investors == 0):
            investors = int(line)
        else:
            days = int(line)

    else:
        inputArray.append(list(map(int, line.split(",")))[1:])

def transpose(matr):
    res = []
    matrN = len(matr)
    matrM = len(matr[0])
    for j in range(matrM):
        tmp = []
        for i in range(matrN):
            tmp = tmp + [matr[i][j]]
        res = res + [tmp]
    matr[:] = res
    return res

def countDegree(y, x):
    return math.degrees(math.atan2(y, x))

def countWeightsByInvestors(matr):
    global investors
    weightLines = [0.0]*investors
    for i in range(investors):
        weightLines[i] = sum(matr[i])
    return weightLines

def countSlopeCoefficient(matr):
    global investors
    increaseDegree = [0.0]*investors
    for i in range(investors):
        increaseDegree[i] = countDegree(matr[i][days - 1] - matr[i][0], days - 1.0)
    return increaseDegree


def getMaxExcept(arr, excepted, current):
    global investors
    curMax = 0
    for i in range(investors):
        if excepted[i] != 0 and i != current and arr[i] > curMax:
            curMax = arr[i]
    return curMax

def countWeights():
    global days, investors, transponedArray, increaseDegree, weightLines
    probabilities = [0] * investors  # текущие накопленные вероятности по всем инвесторам
    probabilitiesDays = [0] * days  # текущая глубина по дням по всем инвесторам

    for i in range(days):
        currentChoice = weightLines.index(max(weightLines))
        currentProbality = transponedArray[i][currentChoice]

        if i > 0:
            currentDepthDay = probabilitiesDays[currentChoice]
            currentDifference = transponedArray[currentDepthDay][currentChoice] - transponedArray[currentDepthDay - 1][currentChoice]
            currentDegree = countDegree(
                                        transponedArray[currentDepthDay][currentChoice] - transponedArray[0][currentChoice],
                                        currentDepthDay - 0
                            )
            currentDegree = countDegree(
                transponedArray[currentDepthDay][currentChoice] - transponedArray[currentDepthDay - 1][currentChoice],
                currentDepthDay - 1
            )

            anotherMax = getMaxExcept(transponedArray[min(probabilitiesDays)], weightLines, currentChoice)
            anotherDegree = abs(increaseDegree[transponedArray[min(probabilitiesDays)].index(anotherMax)] - increaseDegree[currentChoice])
            if currentDegree < increaseDegree[currentChoice]:
                weightLines[currentChoice] = 0
                currentChoice = weightLines.index(max(weightLines))
                currentProbality = transponedArray[probabilitiesDays[currentChoice]][currentChoice]
            elif currentDifference < anotherMax and anotherDegree < 14.88:
                currentChoice = transponedArray[min(probabilitiesDays)].index(anotherMax)
                currentProbality = anotherMax
                transponedArray[probabilitiesDays[currentChoice]][currentChoice] = 0

        # в первый день берем самого потенциально интересного инвестора - лидера
        probabilities[currentChoice] = currentProbality
        probabilitiesDays[currentChoice] += 1

    return probabilities


################################

for line in sys.stdin: # get input strings one by one
    parseLine(line.strip())

########################

increaseDegree = countSlopeCoefficient(inputArray)
weightLines = countWeightsByInvestors(inputArray)
transponedArray = transpose(inputArray)

print(sum(countWeights()))