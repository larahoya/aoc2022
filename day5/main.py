def parseinput():
    # TBD

def getinput():
    return [
        ["T", "D", "W", "Z", "V", "P"],
        ["L", "S", "W", "V", "F", "J", "D"],
        ["Z", "M", "L", "S", "V", "T", "B", "H"],
        ["R", "S", "J"],
        ["C", "Z", "B", "G", "F", "M", "L", "W"],
        ["Q", "W", "V", "H", "Z", "R", "G", "B"],
        ["V", "J", "P", "C", "B", "D", "N"],
        ["P", "T", "B", "Q"],
        ["H", "G", "Z", "R", "C"]
    ]

def gettopitems9000() -> str:
    input = getinput()
    with open('modified_input.txt') as f:
        for line in f.readlines():
            result = line.replace('move', ' ').replace('from', ' ').replace('to', ' ').split()
            quantity, origin, destiny = int(result[0]), int(result[1]) - 1, int(result[2]) - 1
            for _ in range(quantity):
                element = input[origin].pop()
                input[destiny].append(element)
    ans = ""
    for c in input:
        ans = ans + c.pop()
    return ans

def gettopitems9001() -> str:
    input = getinput()
    with open('modified_input.txt') as f:
        for line in f.readlines():
            result = line.replace('move', ' ').replace('from', ' ').replace('to', ' ').split()
            quantity, origin, destiny = int(result[0]), int(result[1]) - 1, int(result[2]) - 1
            temporary = []
            for _ in range(quantity):
                element = input[origin].pop()
                temporary.insert(0, element)
            for e in temporary:
                input[destiny].append(e)
    ans = ""
    for c in input:
        ans = ans + c.pop()
    return ans

