from itertools import permutations as itertools_permutations

filled = '+'
unfilled = 0
width = 18
height = 15
steps = 0

def getFilledLine(arg1, arg2):
    global width
    global unfilled
    totalSum = sum(arg1)
    result = arg1 + [unfilled] * (arg2 - totalSum)
    return result

def cmp(a, b):
    return (a > b) - (a < b) 

def next_permutation(seq, pred = cmp):
    def reverse(seq, start, end):
        end -= 1
        if end <= start:
            return
        while True:
            seq[start], seq[end] = seq[end], seq[start]
            if start == end or start+1 == end:
                return
            start += 1
            end -= 1
    
    if not seq:
        raise StopIteration

    try:
        seq[0]
    except TypeError:
        raise TypeError("seq must allow random access.")
    first = 0
    last = len(seq)
    seq = seq[:]

    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                reverse(seq, next1, last)

                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration


def fastPermutations(arr):
    result = []
    realOrder = list(arr)
    arr.sort()
    try:
        for perm in next_permutation(arr):
            v = list(perm)
            if v not in result and checkPermutation(v) and checkPermutationOrder(v, realOrder):
              result.append(v)
    except:
        return list(map(lambda x: expandPermutation(x, filled), result))
    
def permutations(arr):
    global filled
    global unfilled
    result = []
    for perm in itertools_permutations(arr):
        v = list(perm)
        if v not in result and checkPermutation(v):
         result.append(v)
    
    return list(map(lambda x: expandPermutation(x, filled), result))
    
def checkPermutation(arr):
    for i in range(len(arr) - 1):
        if arr[i] != 0 and arr[i + 1] != 0:
            return False
    return True
    
def checkPermutationOrder(arr, realOrder):
    flexStart = 0
    for r in realOrder:
        if r == 0:
            break
        for i in range(flexStart, len(arr) - 1):
            if r == arr[i]:
                flexStart = i + 1
                break
            if arr[i] != 0 and arr[i] != r:
                return False
    return True
    
def expandPermutation(arr, symbol):
    expandedArray = []
    for element in arr:
        if isinstance(element, int) and element > 0:
            expandedArray.extend([symbol] * element)
        else:
            expandedArray.append(element)
    return expandedArray
    

def checkCrossline(arr1, arr2, pos1, pos2):
    global steps
    steps += 1
    correctPerms1 = []
    correctPerms2 = []
    for perm1 in arr1:
        for perm2 in arr2:
            if perm1[pos2] == perm2[pos1]:
              if perm1 not in correctPerms1:
                correctPerms1.append(perm1)
              if perm2 not in correctPerms2:
                correctPerms2.append(perm2)
    return correctPerms1, correctPerms2
    
def checkCrossline3(arr1, arr2, arr3, pos1, pos2, pos3):
    global steps
    steps += 1
    correctPerms1 = []
    correctPerms2 = []
    correctPerms3 = []
    for perm1 in arr1:
        for perm2 in arr2:
            for perm3 in arr3:
                if perm1[pos2] == perm2[pos1] and perm1[pos3] == perm3[pos1]:
                  if perm1 not in correctPerms1:
                    correctPerms1.append(perm1)
                  if perm2 not in correctPerms2:
                    correctPerms2.append(perm2)
                  if perm3 not in correctPerms3:
                    correctPerms3.append(perm3)
    
    return correctPerms1, correctPerms2, correctPerms3

def getSortedByLengthLines(arr):
    dictKV = {k: len(v) for k, v in enumerate(arr)}
    sortedDict = sorted(dictKV.items(), key=lambda l:l[1])
    return sortedDict

################# 9x9
nonogramLines = [
    [3,4],
    [1,6],
    [1,1,1,1,1,6],
    [3,1,6],
    [5,2,1,2],
    [2,6,1,2,1],
    [1,2,3,2,1],
    [3,1],
    [2,2],
    [3,3],
    [3,3],
    [3,5],
    [3,5],
    [1,1,1],
    [8]
]
nonogramRows = [
    [1,6],
    [3,4],
    [3,2,3],
    [4,3],
    [1,2,2,1],
    [1,3],
    [1,1],
    [1,3],
    [3,2,2,1],
    [1,1,1,4],
    [1,1,3,2,1],
    [1,3,1],
    [5,3],
    [4,2,3],
    [4,4],
    [4],
    [5],
    [6]
]

nonogramLines = list(map(lambda x: getFilledLine(x, width), nonogramLines))
nonogramRows = list(map(lambda x: getFilledLine(x, height), nonogramRows))

nonogramLines = list(map(fastPermutations, nonogramLines))
nonogramRows = list(map(fastPermutations, nonogramRows))


print('======!=======')

for i in range(11):
    linesAsc = getSortedByLengthLines(nonogramLines)
    rowsAsc = getSortedByLengthLines(nonogramRows)
    worstLine = linesAsc[-1]
    worstRow = rowsAsc[-1]
    print(i, worstLine, worstRow)
    if worstLine[1] == 1 and worstRow[1] == 1:
        break
    
    if i%2:
        for l in linesAsc:
            for r in rowsAsc:
                line, row = l[0], r[0]
                if len(nonogramLines[line]) > 1 or len(nonogramRows[row]) > 1:
                        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
    else:
        for l in linesAsc:
            for r in range(len(rowsAsc) - 1):
                line, row1, row2 = l[0], rowsAsc[r][0], rowsAsc[r + 1][0]
                if len(nonogramLines[line]) > 1 or len(nonogramRows[row1]) > 1 or len(nonogramRows[row2]) > 1:
                    nonogramLines[line], nonogramRows[row1], nonogramRows[row2] = checkCrossline3(nonogramLines[line],nonogramRows[row1], nonogramRows[row2],line, row1, row2)


# без > 1 и 1-1 - 1350
#  > 1 и 1-1 - 945
#  > 1 и 1-1/1-2 - no result
print('steps', steps)

print('==============')
for line in range(len(nonogramLines)):
    #print(len(nonogramLines[line])) 
    print(nonogramLines[line][0], len(nonogramLines[line]))
    #print(''.join(nonogramLines[line][0]), len(nonogramLines[line]))
    