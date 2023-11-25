import sys

def drawKey(l):
    lock = list('0' * max(l))
    for kP in l:#l[:-1]:
        lock[kP - 1] = 'X'
    return lock

for line in sys.stdin: # get input strings one by one
    lx = list(map(int, line.split(",")))
    key = "".join(drawKey(lx))

    for i in range(3):
        print(key)

    print("".join(list('X' * max(lx))))