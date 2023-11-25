import sys

def sortByUnicode(s):
    return "".join(s)#ord(s[0])

def BWAlg(line):
    listOfStr = list(line)
    transpositions = [(listOfStr[i:] + listOfStr[:i]) for i in range(len(listOfStr))]
    transpositions.sort(key=sortByUnicode)
    return "".join([t[-1] for t in transpositions])

for line in sys.stdin:
    print(BWAlg(line.strip()))