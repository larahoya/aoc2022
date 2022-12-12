def getvalue(char) -> int:
    if not char.isalpha():
        return 0
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def getprioritiessum() -> int:
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            firstcompartment, secondcompartment = line[:len(line) // 2], line[len(line) // 2:]
            s = set()
            for c in firstcompartment:
                s.add(c)
            for c in secondcompartment:
                if c in s:
                    total += getvalue(c)
                    break
    return total


def getgroupsprioritiessum() -> int:
    total = 0
    with open('input.txt') as f:
        group = []
        group_line = 1
        for line in f.readlines():
            s = set()
            for c in line:
                s.add(c)
            group.append(s)
            if group_line == 3:
                result = set.intersection(*group)
                for c in result:
                    total += getvalue(c)
                group_line = 1
                group = []
            else:
                group_line += 1
    return total
