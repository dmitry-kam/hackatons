latinUpper = ord("A")  # 65
latinLower = ord("a")  # 97

def getWedgeQty(enemyLine, ourLine, ourSum):
    return (getWedgeQty(enemyLine, ourLine - 2, ourSum + ourLine) if (ourLine > 2) else ourSum + ourLine)

print(getWedgeQty(9, 9, 0))

def filterSpaces(s):
    return s != ' '

def handleSymbol(l):
    return ((ord(l) + 1 - latinLower) if (ord(l) >= latinLower) else (ord(l) + 1 - latinUpper))

response = ""

print(list(map(handleSymbol, list(filter(filterSpaces, list("Aahel lo"))))))

vowels = ["a", "e", "i", "o", "u"]
vowels_str = ",".join(vowels)
print(ord("\n"))