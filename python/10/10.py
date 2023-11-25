import sys

def reverseBWTransform(original, handled, stage):
    handled.sort(key=lambda s: "".join(s))
    sortedNew = [i for i in handled]

    if stage > 1:
        # print(original, sortedNew, stage)
        # handled = [(str(i) + original[i] + handled[i]) for i in range(len(handled))]
        for i in range(len(sortedNew)):
            sortedNew[i] = (original[i] + sortedNew[i])
            # print(str(i) + original[i] + "~" + sortedNew[i])
        return reverseBWTransform(original, sortedNew, stage - 1)
    else:
        sortedNew.sort(key=lambda s: s.endswith("|"))
        return "".join(sortedNew.pop())


for line in sys.stdin:
    line = line.strip()
    print(reverseBWTransform(list(line), list(line), len(list(line))))