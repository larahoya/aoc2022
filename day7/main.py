from Models.Node import *


def buildTree() -> Node:
    root = Node("root")
    stack = [root]
    with open('input.txt') as f:
        for line in f.readlines():
            if line.startswith("$ cd /"):
                while len(stack) > 1: stack.pop()
            elif line.startswith("$ cd .."):
                stack.pop()
            elif line.startswith("$ cd"):
                dir_name = line.split()[2]
                current = stack[-1]
                for child in current.children:
                    if child.name == dir_name:
                        stack.append(child)
            elif line.startswith("$ ls"):
                continue
            else:
                current = stack[-1]
                if line.startswith("dir"):
                    _, name = line.split()
                    node = Node(name)
                    current.children.append(node)
                else:
                    size, name = line.split()
                    node = Node(name, False, size)
                    current.children.append(node)
    return root


def getsum(node: Node, maxsize: int) -> int:
    total = 0
    if node.isdir:
        for child in node.children:
            total += getsum(child, maxsize)
        if node.size <= maxsize:
            total += node.size
    return total


def getdirectories(node: Node, minsize: int) -> list[int]:
    result = []
    if node.isdir:
        if node.size >= minsize:
            result.append(node.size)
        for child in node.children:
            result += getdirectories(child, minsize)
    return result


def part2() -> int:
    root = buildTree()
    root.getsize()
    free = 70000000 - root.size
    needed = 30000000 - free
    directories = getdirectories(root, needed)
    return min(directories)


def part1() -> int:
    root = buildTree()
    root.getsize()
    return getsum(root, 100000)
