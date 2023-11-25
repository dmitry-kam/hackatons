import sys

alphabet = []
rightTop = []
leftDown = []
iterator = 0
squareSide = 0

def parseString(s):
    return s.strip().split(",")


def handleIJ(l):
    return "I/J" if l == "I" or l == "J" else l

def cryptBigram(b):
    if (len(b) == 1):
        return b
    elif (len(b) == 2):
        letter1, letter2 = list(map(handleIJ, list(b)))

        indexLT = indexRD = []
        for i in range(0, squareSide):
            if letter1 in alphabet[i]:
                indexLT = [i, alphabet[i].index(letter1)]
            if letter2 in alphabet[i]:
                indexRD = [i, alphabet[i].index(letter2)]
            if indexLT != [] and indexRD != []:
                break
        # print(letter1, letter2, indexLT, indexRD, rightTop[indexLT[0]][indexRD[1]], leftDown[indexRD[0]][indexLT[1]])
        return rightTop[indexLT[0]][indexRD[1]] + leftDown[indexRD[0]][indexLT[1]]
    else:
        return ""


def crypt4Squares(s):
    s = list(s.strip().upper().replace(" ", ""))
    bigrams = [s[i] + (s[i + 1] if i < len(s) - 1 else "") for i in range(0, len(s), 2)]
    return "".join(list(map(cryptBigram, bigrams)))


for line in sys.stdin:
    if len(line) > 1:
        # print(iterator, line)
        elArr = parseString(line)
        if iterator == 0:
            squareSide = len(elArr)
        if iterator < squareSide:
            alphabet.append(elArr)
        elif squareSide <= iterator < 2 * squareSide:
            rightTop.append(elArr)
        elif 2 * squareSide <= iterator < 3 * squareSide:
            leftDown.append(elArr)
        elif iterator == 4 * squareSide:
            del iterator
            print(crypt4Squares(line))
            break
        iterator += 1