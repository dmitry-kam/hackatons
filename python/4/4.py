import sys

def RLE(line):
    listOfStr = list(line)
    listOfStrLength = len(listOfStr)
    dictOfWords = { i : listOfStr[i] for i in range(0, len(listOfStr))}
    #print(dictOfWords)
    for s in range(1, len(listOfStr)):
        if (listOfStr[s - 1] == listOfStr[s]):
            dictOfWords.pop(s)
    keys = list(dictOfWords.keys()) + [listOfStrLength]
    qtyArr = [keys[i] - keys[i - 1] for i in range(1, len(keys))]
    response = list(map(lambda qty, symbol: str(qty)+str(symbol), qtyArr, dictOfWords.values()))
    return ",".join(response)

for line in sys.stdin:
    print(RLE(line.strip()))