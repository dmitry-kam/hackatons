from itertools import permutations as itertools_permutations
#import itertools
import time

start = time.time()

filled = '¦'
unfilled = '_'
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
            if perm1[pos1] == perm2[pos2]:
              if perm1 not in correctPerms1:
                correctPerms1.append(perm1)
              if perm2 not in correctPerms2:
                correctPerms2.append(perm2)
                break
    return correctPerms1, correctPerms2 



# Пример использования:
array = getFilledLine([1, 2, 3], 8)
#print(array)
#print(permutations(array))

# print(checkCrossline(permutations(array), [['+', '-', '-', '+', '-', '+', '+', '+']], 2,2))

array = getFilledLine([9], 9)
print(permutations(array))

#################
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

#################
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

#print((permutations([3,'-','-','-','-','-','-'])))
###################
'''
end = time.time()
length = end - start
print("1", length, "seconds!")
print((nonogramLines))
end = time.time()

length = end - start
print("2", length, "seconds!")
print((nonogramLines[0]))

end = time.time()
length = end - start
print("3", length, "seconds!")
end = time.time()
length = end - start
print("4", length, "seconds!")
print(len(nonogramLines))

'''

'''
print((nonogramLines[0]))
print(len(nonogramLines[0]))
print(len(nonogramRows[0]))
x, y = checkCrossline(nonogramLines[0],nonogramRows[0],0, 0)
print(len(x))
print('----------')
print(len(y))

'''
for line in range(len(nonogramLines)):
    for row in range(len(nonogramRows)):
        #print(line, row)
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)
        
for line in range(len(nonogramLines)):
    for row in range(len(nonogramRows)):
        nonogramLines[line], nonogramRows[row] = checkCrossline(nonogramLines[line],nonogramRows[row],line, row)        

for line in range(len(nonogramLines)):
    print(nonogramLines[line])
print('----------')
for row in range(len(nonogramRows)):
    print(''.join(nonogramRows[row][0]))  