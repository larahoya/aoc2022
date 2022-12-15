class Node:
    def __init__(self, name: str, isdir: bool = True, size: int = 0):
        self.name = name
        self.isdir = isdir
        self.size = int(size)
        self.children = list[Node]()

    def getsize(self) -> int:
        if self.isdir:
            total = 0
            for child in self.children:
                total += child.getsize()
            self.size = total
            return total
        else:
            return self.size
