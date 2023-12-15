import aocd

f = aocd.get_data(day=13, year=2023)
total = 0


def findMirrorIndex(s):
    mirror_index = []
    for colPos in range(1, len(s)):
        left = s[:colPos]
        reverse_left = left[::-1]
        right = s[colPos:]
        if reverse_left.startswith(right) or right.startswith(reverse_left):
            mirror_index.append(colPos)
    return mirror_index


for index, pattern in enumerate(f.split("\n\n")):
    grid = str(pattern).splitlines()

    mirrorColIndex = set(range(len(grid[0])))
    for row in grid:
        mirrorColIndex = mirrorColIndex.intersection(findMirrorIndex(row))

    rotatedGrid = list(map("".join, zip(*grid)))
    mirrorRowIndex = set(range(len(rotatedGrid[0])))
    for row in rotatedGrid:
        mirrorRowIndex = mirrorRowIndex.intersection(findMirrorIndex(row))

    total += list(mirrorColIndex)[0] if mirrorColIndex else 100 * list(mirrorRowIndex)[0]

print(f"Total is {total}.")
