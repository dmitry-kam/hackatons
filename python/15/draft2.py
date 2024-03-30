from itertools import permutations as itertools_permutations
#import itertools
#import time
#start = time.time()

filled = '+' #'¦'
unfilled = '-'
width = 10
height = 12

    
# arg1 - array of int (sequences)
# arg2 - int, length of line
def getFilledLine(arg1, arg2):
    global width
    global unfilled
    totalSum = sum(arg1)
    result = arg1 + [unfilled] * (arg2 - totalSum)
    return result

def permutations(arr):
    global filled
    global unfilled
    result = []
    for perm in itertools_permutations(arr):
        v = list(perm)
        if v not in result and checkPermutation(v): 
         #result.append(expandPermutation(v, filled))
         result.append(v)
    
    return list(map(lambda x: expandPermutation(x, filled), result))
    
def checkPermutation(arr):
    for i in range(len(arr) - 1):
        if isinstance(arr[i], int) and isinstance(arr[i + 1], int):
            return False
    return True
    
def expandPermutation(arr, symbol):
    expandedArray = []
    for element in arr:
        if isinstance(element, int):
            expandedArray.extend([symbol] * element)
        else:
            expandedArray.append(element)
    return expandedArray
    

def checkCrossline(arr1, arr2, pos1, pos2):
    correctPerms1 = []
    correctPerms2 = []
    for perm1 in arr1:
        for perm2 in arr2:
            if perm1[pos2] == perm2[pos1]:
              if perm1 not in correctPerms1:
                correctPerms1.append(perm1)
              if perm2 not in correctPerms2:
                correctPerms2.append(perm2)
                #break
    return correctPerms1, correctPerms2

def getSortedByLengthLines(arr):
    dictKV = {k: len(v) for k, v in enumerate(arr)}
    sortedDict = sorted(dictKV.items(), key=lambda l:l[1])
    return sortedDict

################# 9x9
nonogramLines = [
    [3],
    [1,2],
    [5],
    [2],
    [2,1],
    [9],
    [2,4],
    [4,2],
    [5]
]
nonogramRows = [
    [1,3],
    [3,5],
    [1,4,2],
    [4,1,2],
    [2,2,1],
    [4],
    [3],
    [3],
    [1]
]


nonogramLines = list(map(lambda x: getFilledLine(x, 9), nonogramLines))
nonogramRows = list(map(lambda x: getFilledLine(x, 9), nonogramRows))

nonogramLines = list(map(permutations, nonogramLines))
nonogramRows = list(map(permutations, nonogramRows))

print(getSortedByLengthLines(nonogramLines))
print(getSortedByLengthLines(nonogramRows))

linesAsc = getSortedByLengthLines(nonogramLines)
rowsAsc = getSortedByLengthLines(nonogramRows)

'''
print('======!=======')
for line in nonogramLines[5]:
    print(line)
print('======!=======')

for line in nonogramRows[0]:
    print(line[5] == '+' , line)
print('======!=======')
print('======!=======')

h1, h2 = checkCrossline(nonogramLines[5],nonogramRows[0],5, 0)

print('======!=======')
print(h1)
print(h2)
print('======!=======')
exit()
'''

'''
print(nonogramLines[0])
print('----------')
print(nonogramRows[0])
print('----------')

x = [['+', '+', '+', '-', '-', '-', '-', '-', '-'], ['-', '+', '+', '+', '-', '-', '-', '-', '-'], ['-', '-', '+', '+', '+', '-', '-', '-', '-'], ['-', '-', '-', '+', '+', '+', '-', '-', '-'], ['-', '-', '-', '-', '+', '+', '+', '-', '-'], ['-', '-', '-', '-', '-', '+', '+', '+', '-'], ['-', '-', '-', '-', '-', '-', '+', '+', '+']]
y = [['-', '-', '+', '-', '-', '+', '+', '+', '-']]
print(checkCrossline(x,y,0, 0))
'''

for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)

for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        #print('line ', line, 'row ', row, len(nonogramLines[line]), len(nonogramRows[row]))
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
        #print(len(nonogramLines[line]), len(nonogramRows[row]))

for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        print('line ', line, 'row ', row, len(nonogramLines[line]), len(nonogramRows[row]))
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
        print(len(nonogramLines[line]), len(nonogramRows[row]))



print('==============')
for line in range(len(nonogramLines)):
    print(''.join(nonogramLines[line][0]), len(nonogramLines[line]))
    
    
'''
print('==============')

for line in range(len(nonogramLines)):
    for row in range(len(nonogramRows)):
        print('line ', line, 'row ', row, len(nonogramLines[line]), len(nonogramRows[row]))
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
        print(len(nonogramLines[line]), len(nonogramRows[row]))
        #break
            
print(nonogramLines[0])
print(nonogramRows[0])

print('==============')
for line in range(len(nonogramLines)):
    print(''.join(nonogramLines[line][0]), len(nonogramLines[line]))
print('==============')
for row in range(len(nonogramRows)):
    print(''.join(nonogramRows[row][0]))  
'''