from itertools import permutations as itertools_permutations
#import itertools
#import time
#start = time.time()

filled = '+' #'¦'
unfilled = 0 #'-'
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

def cmp(a, b):
    return (a > b) - (a < b) 

def next_permutation(seq, pred = cmp):
    """Like C++ std::next_permutation() but implemented as
    generator. Yields copies of seq."""

    def reverse(seq, start, end):
        # seq = seq[:start] + reversed(seq[start:end]) + \
        #       seq[end:]
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

    # Yield input sequence as the STL version is often
    # used inside do {} while.
    yield seq
    
    if last == 1:
        raise StopIteration

    while True:
        next = last - 1

        while True:
            # Step 1.
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                # Step 2.
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                # Step 3.
                reverse(seq, next1, last)

                # Change to yield references to get rid of
                # (at worst) |seq|! copy operations.
                yield seq[:]
                break
            if next == first:
                raise StopIteration
    raise StopIteration


def fastPermutations(arr):
    result = []
    arr.sort()
    #print('+', arr.sort())
    try:
        for perm in next_permutation(arr):
            v = list(perm)
            #print('+', perm, type(v), perm in result, checkPermutation(perm))
            if v not in result and checkPermutation(v):
              result.append(v)
    except:
        #print(result)
        return list(map(lambda x: expandPermutation(x, filled), result))
        #print("An exception occurred")
    
def permutations(arr):
    global filled
    global unfilled
    result = []
    print(itertools_permutations(arr))
    for perm in itertools_permutations(arr):
        v = list(perm)
        if v not in result and checkPermutation(v): 
         #result.append(expandPermutation(v, filled))
         result.append(v)
    
    return list(map(lambda x: expandPermutation(x, filled), result))
    
def checkPermutation(arr):
    for i in range(len(arr) - 1):
        #print('-', arr[i] != 0)
        #print('-', arr[i + 1] != 0)
        if arr[i] != 0 and arr[i + 1] != 0:
        #if isinstance(arr[i], int) and isinstance(arr[i + 1], int) and arr[i] != 0 and arr[i + 1] != 0:
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
    correctPerms1 = []
    correctPerms2 = []
    #print(len(arr1), len(arr2))
    for perm1 in arr1:
        for perm2 in arr2:
            if perm1[pos2] == perm2[pos1]:
              #print(perm1)
              #print(perm2)
              #print(pos1)
              #print(pos2)
              #print(perm1[pos2] == perm2[pos1])
              if perm1 not in correctPerms1:
                correctPerms1.append(perm1)
              if perm2 not in correctPerms2:
                correctPerms2.append(perm2)
                #break
    
    #print(len(correctPerms1), len(correctPerms2))        
    #exit()
    return correctPerms1, correctPerms2
    
def checkCrossline3(arr1, arr2, arr3, pos1, pos2, pos3):
    correctPerms1 = []
    correctPerms2 = []
    correctPerms3 = []
    #print(len(arr1), len(arr2), len(arr3))
    for perm1 in arr1:
        for perm2 in arr2:
            for perm3 in arr3:
                if perm1[pos2] == perm2[pos1] and perm1[pos3] == perm3[pos1]:
                  #print(perm1)
                  #print(perm2)
                  #print(pos1)
                  #print(pos2)
                  #print(perm1[pos2] == perm2[pos1])
                  if perm1 not in correctPerms1:
                    correctPerms1.append(perm1)
                  if perm2 not in correctPerms2:
                    correctPerms2.append(perm2)
                  if perm3 not in correctPerms3:
                    correctPerms3.append(perm3)
    
    #print(len(correctPerms1), len(correctPerms2), len(correctPerms3))        
    #exit()
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
    [17]
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

nonogramRows = [
    [1,6,1],
    [3,4,1],
    [3,2,3,1],
    [4,3,1],
    [1,2,2,1,1],
    [1,3,1],
    [1,1,1],
    [1,3,1],
    [3,2,2,1,1],
    [1,1,1,4,1],
    [1,1,3,2,1,1],
    [1,3,1,1],
    [5,3,1],
    [4,2,3,1],
    [4,4,1],
    [4,1],
    [5,1],
    [6,1]
]

nonogramLines = list(map(lambda x: getFilledLine(x, 18), nonogramLines))
nonogramRows = list(map(lambda x: getFilledLine(x, 15), nonogramRows))

#nonogramLines1 = list(map(lambda x: getFilledLine(x, 18), nonogramLines))
#nonogramRows1 = list(map(lambda x: getFilledLine(x, 15), nonogramRows))


#print(nonogramLines[4])

#print(fastPermutations([8, 0, 0, 0, 0, 0, 0, 0, 0]))
#exit()
nonogramLines = list(map(fastPermutations, nonogramLines))
nonogramRows = list(map(fastPermutations, nonogramRows))
#nonogramLines = list(map(next_permutation, nonogramLines))
#nonogramRows = list(map(next_permutation, nonogramRows))


print('======!=======')

linesAsc = getSortedByLengthLines(nonogramLines)
rowsAsc = getSortedByLengthLines(nonogramRows)


#print(nonogramLines[14])
print(linesAsc)
print(rowsAsc)
'''
exit()
'''

for l in linesAsc:
    for r in range(len(rowsAsc) - 1):
        #print(l,r, rowsAsc[r][0], rowsAsc[r][1])
        line, row1, row2 = l[0], rowsAsc[r][0], rowsAsc[r + 1][0]
        if len(nonogramLines[line]) != 1 and len(nonogramRows[row1]) != 1 and len(nonogramRows[row2]) != 1:
            nonogramLines[line], nonogramRows[row1], nonogramRows[row2] = checkCrossline3(nonogramLines[line],nonogramRows[row1], nonogramRows[row2],line, row1, row2)

linesAsc = getSortedByLengthLines(nonogramLines)
rowsAsc = getSortedByLengthLines(nonogramRows)
print(linesAsc)
print(rowsAsc)

'''
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        #if line == 10:
        #    exit()
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            #print(nonogramLines[line])
            #print(nonogramRows[row])
            #a, b = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
            #print(a, b)
            #exit()
            #print('>', len(nonogramLines[line]), len(nonogramRows[row]), line, row)
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
            #print('<', len(nonogramLines[line]), len(nonogramRows[row]), line, row)


for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)

for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
            
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
            

for l in linesAsc:
    for r in rowsAsc:
        line, row = l[0], r[0]
        if len(nonogramLines[line]) > 1 and len(nonogramRows[row]) > 1:
            line, row = l[0], r[0]
            #print('line ', line, 'row ', row, len(nonogramLines[line]), len(nonogramRows[row]))
            nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
            #print(len(nonogramLines[line]), len(nonogramRows[row]))
'''

print('==============')
for line in range(len(nonogramLines)):
    #print(len(nonogramLines[line])) 
    print(nonogramLines[line][0], len(nonogramLines[line]))
    #print(''.join(nonogramLines[line][0]), len(nonogramLines[line]))
    