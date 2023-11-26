import string

latinUpper = ord("A")  # 65
latinLower = ord("a")  # 97
inCharSet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"

def handleLine(line):
    line = line.strip()
    words = separatorsHandle(line, 1).split(" ")

    words = list(map(cryptWord, words))
    print(words)
    return separatorsHandle(" ".join(words), 0)

def cryptWord(w):
    return w if w in ['?', '!', '.', ',', ':', ';'] else caesar(mix(w))

def separatorsHandle(line, mode):
    for sep in ['?', '!', '.', ',', ':', ';']:
        line = line.replace(sep, " " + sep) if mode == 1 else line.replace(" " + sep, sep)
    return line

def countSpaces(arr):
    return arr.count("_")
def mix(line):
    length = len(line)
    if length == 1:
        return line
    mixRes = ['_'] * length
    k, steps, inserts, direction = 1, 2, 0, 1

    while countSpaces(mixRes):
        #print(line[length - countSpaces(mixRes)], k, direction, inserts, steps, countSpaces(mixRes))
        if 0 <= k < length:
            if mixRes[k] == '_':
                if inserts%steps == 0:
                    mixRes[k] = line[len(line) - countSpaces(mixRes)]
                inserts += 1
        else:
            if k >= length:
                k = length - 1
                direction = -1
            else:
                k = 0
                direction = 1

        k += direction

    return "".join(mixRes)

def caesar(line):
    global latinUpper, latinLower, inCharSet
    firstL = ord(line[0])
    shift = 2*(firstL + 1 - latinLower if latinLower <= firstL else firstL + 1 - latinUpper)

    outCharSet = "".join(inCharSet[shift:] + inCharSet[:shift])

    caesarDict = str.maketrans(inCharSet, outCharSet)
    return line.translate(caesarDict)

test = "When you delete something, you are making a choice to destroy it. To never see it again."

print(handleLine(test))