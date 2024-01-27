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
    #print("curMax", curMax)
    return curMax

def countWeights():
    global days, investors, transponedArray, increaseDegree, weightLines
    resultWeights = [[0.0] * investors] * days
    probabilities = [0] * investors  # текущие накопленные вероятности по всем инвесторам
    probabilitiesDays = [0] * days  # текущая глубина по дням по всем инвесторам

    for i in range(days):
        # выбираем самую абсолютно большую вероятность
        currentChoice = weightLines.index(max(weightLines))
        currentProbality = transponedArray[i][currentChoice]
        print(">>currentChoice", currentChoice + 1, "currentProbality", currentProbality)

        if i > 0:
            currentDepthDay = probabilitiesDays[currentChoice]
            currentDifference = transponedArray[currentDepthDay][currentChoice] - transponedArray[currentDepthDay - 1][currentChoice]
            # сравниваем текущий угловой коэффициент с общим по инвестору-лидеру (берем в расчет его день по глубине, а не текущий)
            # currentDegree = countDegree(
            #                             transponedArray[currentDepthDay][currentChoice] - transponedArray[0][currentChoice],
            #                             currentDepthDay - 0
            #                 )

            # смотрим на угловой коэффициент для текущего дня по инвестору
            currentDegree = countDegree(
                transponedArray[currentDepthDay][currentChoice] - transponedArray[currentDepthDay - 1][currentChoice],
                currentDepthDay - 1
            )

            anotherMax = getMaxExcept(transponedArray[min(probabilitiesDays)], weightLines, currentChoice)
            #anotherDegree = abs(increaseDegree[transponedArray[min(probabilitiesDays)].index(anotherMax)] - increaseDegree[currentChoice])
            anotherDegree = abs(increaseDegree[transponedArray[min(probabilitiesDays)].index(anotherMax)] - increaseDegree[currentChoice])
            print("===========", anotherDegree, currentDifference, anotherMax)
            # если угловой коэффициент меньше, чем текущий, то меняем инвестора
            if currentDegree < increaseDegree[currentChoice]:
                # сбрасываем вес по текущему инвестору
                weightLines[currentChoice] = 0
                # меняем лидера
                currentChoice = weightLines.index(max(weightLines))
                currentProbality = transponedArray[probabilitiesDays[currentChoice]][currentChoice]

                print(weightLines)
                print("Change by slope", i + 1, " IS investor", currentChoice + 1, " CurDay  ", currentDepthDay, " with  ", currentDegree)

            # если угловые коэффициенты не сильно расходятся и
            # если в текущий день переключение на нового инвестора в абсолюте выгоднее, то меняем без сброса
            elif currentDifference < anotherMax and anotherDegree < 14.88:
                currentChoice = transponedArray[min(probabilitiesDays)].index(anotherMax)
                currentProbality = anotherMax
                # сбрасываем вес в том дне, в котором использовали этот максимум
                transponedArray[probabilitiesDays[currentChoice]][currentChoice] = 0
                print("Change by absolute", i + 1, " IS investor", currentChoice + 1, " with  ", currentProbality, anotherMax, min(probabilitiesDays))

        # в первый день берем самого потенциально интересного инвестора - лидера
        probabilities[currentChoice] = currentProbality
        probabilitiesDays[currentChoice] += 1


        print(i + 1, "-----max in day", " IS investor", currentChoice + 1, " with  ", increaseDegree[currentChoice])
    return probabilities

    for i in range(days):
        print("-----------------------------------")
        investors = [0.0] * investors
        degrees = [0.0] * investors
        for j in range(investors):
            # investors[j] = (increaseDegree[j] / 90 * i) + transponedArray[i][j] - (transponedArray[i - 1][j] if i > 1 else 0)

            # maxxx = transponedArray[i][j] - (transponedArray[i - 1][j] if i > 1 else 0)
            maxxx = transponedArray[probabilitiesDays[j]][j] - (
                transponedArray[probabilitiesDays[j] - 1][j] if probabilitiesDays[j] > 1 else 0)
            # сравниваем текущий угловой коэффициент с общим по инвестору
            ghghgh = math.degrees(math.atan2(transponedArray[probabilitiesDays[j]][j] - (
                transponedArray[probabilitiesDays[j] - 1][j] if probabilitiesDays[j] > 1 else 0),
                                             probabilitiesDays[j] - 1.0))
            # считаем абсолютный профит по вероятности (уже взятый и потенциальный)
            sgsdg = (transponedArray[i][j] - probabilities[j])  # ghghgh +

            degrees[j] = (ghghgh / increaseDegree[j])
            # investors[j] = ghghgh / increaseDegree[j]
            investors[j] = maxxx - probabilities[j]  # + (increaseDegree[j] / 90) #/ increaseDegree[j]

            # print(">>>", i, j, transponedArray[i], increaseDegree[j], investors[j])
        # investors = transponedArray[i]
        resultWeights[i] = investors
        probabilities[investors.index(max(investors))] = max(investors)
        probabilitiesDays[investors.index(max(investors))] += 1
        print("!!!!max in day", i + 1, " IS investor", investors.index(max(investors)) + 1, " with  ", max(investors))
        print(">>>", investors)
        print("???", degrees)
    return resultWeights

########################

investors = 4   # investors
days = 5   # days

inputArray = [
    [1.0,2.0,3.0,4.0,6.0],
    [2.0,3.0,3.0,4.0,6.0],
    [3.0,4.0,5.0,5.0,5.0],
    [6.0,7.0,7.0,7.0,9.0],
]

investors = 4   # investors
days = 7   # days

inputArray = [
     [1, 1, 1, 2, 2, 2, 2],
     [2, 3, 3, 3, 3, 3, 3],
     [1, 2, 3, 4, 5, 6, 7],
     [1, 1, 1, 1, 1, 1, 1]
]


increaseDegree = countSlopeCoefficient(inputArray)
weightLines = countWeightsByInvestors(inputArray)
print(":::::", increaseDegree)
print("!!!!", weightLines)

transponedArray = transpose(inputArray)

print(countWeights())
################################






######

# for line in sys.stdin: # get input strings one by one
#     parseLine(line.strip())
#
#
# print(days)
# print(investors)
# print(inputArray)