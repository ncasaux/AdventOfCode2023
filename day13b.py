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
    grid = [list(l) for l in str(pattern).splitlines()]

    originalMirrorColIndex = set(range(len(grid[0])))
    for row in grid:
        originalMirrorColIndex = originalMirrorColIndex.intersection(findMirrorIndex("".join(row)))

    rotatedGrid = list(map("".join, zip(*grid)))
    originalMirrorRowIndex = set(range(len(rotatedGrid[0])))
    for row in rotatedGrid:
        originalMirrorRowIndex = originalMirrorRowIndex.intersection(findMirrorIndex("".join(row)))

    newMirrorColIndex = set()
    newMirrorRowIndex = set()

    for r in range(len(grid)):
        for c in range(len(grid[r])):

            grid[r][c] = "." if grid[r][c] == "#" else "#"

            mirrorColIndex = set(range(len(grid[0])))
            for row in grid:
                mirrorColIndex = mirrorColIndex.intersection(findMirrorIndex("".join(row)))

            rotatedGrid = list(map("".join, zip(*grid)))
            mirrorRowIndex = set(range(len(rotatedGrid[0])))
            for row in rotatedGrid:
                mirrorRowIndex = mirrorRowIndex.intersection(findMirrorIndex("".join(row)))

            mirrorColIndex = mirrorColIndex.difference(originalMirrorColIndex)
            if mirrorColIndex:
                newMirrorColIndex = mirrorColIndex

            mirrorRowIndex = mirrorRowIndex.difference(originalMirrorRowIndex)
            if mirrorRowIndex:
                newMirrorRowIndex = mirrorRowIndex

            grid[r][c] = "." if grid[r][c] == "#" else "#"

    if newMirrorColIndex:
        total += list(newMirrorColIndex)[0]
    if newMirrorRowIndex:
        total += 100 * list(newMirrorRowIndex)[0]

print(f"Total is {total}.")
