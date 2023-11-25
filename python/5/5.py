import sys
import string


def clearStr(line):
    inCharSet = "!@#$%^&*()[]{};:,./<>?\|`~-=_+\""
    outCharSet = "." * len(inCharSet)
    splCharReplaceList = str.maketrans(inCharSet, outCharSet)
    return line.translate(splCharReplaceList)


def nameUnion(a, b):
    cyrA = ord("А")
    cyrZ = ord("Я")
    return (str(a) + " " + str(b)).replace('.', '') if (
                cyrA <= ord(a[0]) <= cyrZ and cyrA <= ord(b[0]) <= cyrZ and '.' not in a) else ""


def getFullnames(line):
    wordArr = list(filter(lambda s: s != "", clearStr(line.strip()).split(" ")))
    # print(wordArr)
    response = filter(lambda s: s != "", list(map(nameUnion, wordArr[:-1], wordArr[1:])))
    return ", ".join(response)


for line in sys.stdin:
    print(getFullnames(line))