import heapq

def getmaxcalories() -> int:
    with open('input.txt') as f:
        max_calories = 0
        total = 0
        for line in f.readlines():
            if line in ['\n', '\r\n']:
                max_calories = max(max_calories, total)
                total = 0
            else:
                total += int(line)
        max_calories = max(max_calories, total)
        return max_calories

def getthreemaxcalories() -> int:
    min_heap = []
    with open('input.txt') as f:
        total = 0
        for line in f.readlines():
            if line in ['\n', '\r\n']:
                if len(min_heap) < 3:
                    heapq.heappush(min_heap, total)
                elif min_heap[0] < total:
                    heapq.heappushpop(min_heap, total)
                total = 0
            else:
                total += int(line)
        return sum(min_heap)
