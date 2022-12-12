def findoverlaps() -> int:
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            result = line.replace('-', ' ').replace(',', ' ').split()
            start_a, end_a, start_b, end_b = int(result[0]), int(result[1]), int(result[2]), int(result[3])
            if not ((end_a < start_b) or (end_b < start_a)):
                total += 1
    return total

def findcontains() -> int:
    total = 0
    with open('input.txt') as f:
        for line in f.readlines():
            result = line.replace('-', ' ').replace(',', ' ').split()
            start_a, end_a, start_b, end_b = int(result[0]), int(result[1]), int(result[2]), int(result[3])
            if (start_a <= start_b and end_a >= end_b) or (start_b <= start_a and end_b >= end_a):
                total += 1
    return total

