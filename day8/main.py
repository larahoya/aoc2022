def buildarrays() -> list[list[int]]:
    grid = []
    with open('input.txt') as f:
        for line in f.readlines():
            a = []
            for char in line:
                if char.isnumeric():
                    a.append(int(char))
            grid.append(a)
    return grid


def getscore(x: int, y: int, grid: list[list[int]]) -> int:
    size = len(grid)
    tree_height = grid[x][y]

    # left
    left = 0
    for j in range(y-1, -1, -1):
        if grid[x][j] < tree_height:
            left += 1
        else:
            left += 1
            break

    # right
    right = 0
    for j in range(y+1, size):
        if grid[x][j] < tree_height:
            right += 1
        else:
            right += 1
            break

    # top
    top = 0
    for i in range(x-1, -1, -1):
        if grid[i][y] < tree_height:
            top += 1
        else:
            top += 1
            break

    # bottom
    bottom = 0
    for i in range(x+1, size):
        if grid[i][y] < tree_height:
            bottom += 1
        else:
            bottom += 1
            break

    return right * left * bottom * top

def part2() -> int:
    result = 0
    grid = buildarrays()
    size = len(grid)

    for i in range(size):
        for j in range(size):
            score = getscore(i, j, grid)
            result = max(result, score)

    return result

def part1():
    grid = buildarrays()
    size = len(grid)
    result = set()

    # left -> right i+, j+
    for i in range(size):
        prev = -1
        for j in range(size):
            if grid[i][j] > prev:
                result.add((i, j))
                prev = grid[i][j]

    # bottom -> top j+, i-
    for j in range(size):
        prev = -1
        for i in range(size - 1, -1, -1):
            if grid[i][j] > prev:
                result.add((i, j))
                prev = grid[i][j]

    # right -> left i-, j-
    for i in range(size - 1, -1, -1):
        prev = -1
        for j in range(size - 1, -1, -1):
            if grid[i][j] > prev:
                result.add((i, j))
                prev = grid[i][j]

    # top -> bottom j-, i+
    for j in range(size - 1, -1, -1):
        prev = -1
        for i in range(size):
            if grid[i][j] > prev:
                result.add((i, j))
                prev = grid[i][j]

    return len(result)
