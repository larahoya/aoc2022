def getscore() -> int:
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            p = line.split()
            if p[1] == "X":
                score += 1
                if p[0] == "A": score += 3
                elif p[0] == "B": score += 0
                else: score += 6
            elif p[1] == "Y":
                score += 2
                if p[0] == "A": score += 6
                elif p[0] == "B": score += 3
                else: score += 0
            else:
                score += 3
                if p[0] == "A": score += 0
                elif p[0] == "B": score += 6
                else: score += 3
    return score


def getplay() -> int:
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            p = line.split()
            if p[1] == "X":
                score += 0
                if p[0] == "A":
                    score += 3
                elif p[0] == "B":
                    score += 1
                else:
                    score += 2
            elif p[1] == "Y":
                score += 3
                if p[0] == "A":
                    score += 1
                elif p[0] == "B":
                    score += 2
                else:
                    score += 3
            else:
                score += 6
                if p[0] == "A":
                    score += 2
                elif p[0] == "B":
                    score += 3
                else:
                    score += 1
    return score
