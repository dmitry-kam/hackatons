import sys

tree = {}
qtySixLength = 0


class leaf():
    global tree

    def init(self, num):
        self.number = int(num)
        self.children = []

    def index(self):
        return self.number

    def addChild(self, child):
        # print("I am ", self.number, "I add child ", child.index())
        self.children.append(child)

    def getChildren(self):
        return self.children

    def getFirstChildren(self):
        return self.children[0]

    def childrenQty(self):
        return len(self.children)


def handleStr(line):
    line = line.strip()
    if (len(line)):
        s = line.replace(':', ',').split(",")
        leafs = list(map(leaf, s))
        parentIndex = None
        for l in leafs:
            lIndex = l.index()
            if lIndex not in tree and len(tree) > 0:
                tree[lIndex] = l
                if (parentIndex != None):
                    tree[parentIndex].addChild(tree[lIndex])
                    # print("Add in parent", lIndex, "->", parentIndex)
            elif len(tree) == 0:
                parentIndex = lIndex
                tree[lIndex] = l
                # print("Root", parentIndex)
            elif lIndex in tree:
                parentIndex = lIndex
                # print("Parent", parentIndex)


def countLeafs(l, trekLength):
    global tree
    global qtySixLength
    if trekLength >= 6:
        qtySixLength += 1
        return True
    elif isinstance(l, leaf):
        # print("I'm ", l.index(), trekLength)
        if l.childrenQty():
            [countLeafs(ch, trekLength + 1) for ch in l.getChildren()]
        else:
            return countLeafs(False, trekLength + 1)
    else:
        return False


for line in sys.stdin:
    handleStr(line)

# first in recursion
for leafV in tree.values():
    countLeafs(leafV, 0)
    break

print(qtySixLength)