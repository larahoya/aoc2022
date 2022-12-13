def getposition(content: str, n: int) -> int:
    s = set()
    h = {}
    start, end = 0, 0
    while end - start <= n-1:
        s.add(content[end])
        if content[end] not in h:
            h[content[end]] = 0
        h[content[end]] += 1
        end += 1
    while len(s) < n:
        h[content[start]] -= 1
        if h[content[start]] == 0:
            del h[content[start]]
            s.remove(content[start])
        if content[end] not in h:
            h[content[end]] = 0
        h[content[end]] += 1
        s.add(content[end])
        start += 1
        end += 1
    return end

def getstartofpackage() -> int:
    with open('input.txt') as f:
        content = f.read()
        position = getposition(content, 4)
    return position

def getstartofmessage() -> int:
    with open('input.txt') as f:
        content = f.read()
        position = getposition(content, 14)
    return position
