import aocd

f = aocd.get_data(day=11, year=2023)
# f = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""
rowIndex = colIndex = None
gs = []
distances = []

for rowIndex, currentLine in enumerate(f.splitlines()):
    for colIndex, currentChar in enumerate(currentLine):
        if currentChar == "#":
            gs.append((rowIndex, colIndex))

galaxiesRow = set([galaxy[0] for galaxy in gs])
galaxiesCol = set([galaxy[1] for galaxy in gs])

emptyRow = galaxiesRow.symmetric_difference(range(rowIndex + 1))
emptyCol = galaxiesCol.symmetric_difference(range(colIndex + 1))

for g in range(len(gs)):
    for h in range(g + 1, len(gs)):
        rowIntersect = emptyRow.intersection(range(min(gs[g][0], gs[h][0]), max(gs[g][0], gs[h][0])))
        colIntersect = emptyCol.intersection(range(min(gs[g][1], gs[h][1]), max(gs[g][1], gs[h][1])))
        dist = abs(gs[h][0] - gs[g][0]) + 999999 * len(rowIntersect) + abs(gs[h][1] - gs[g][1]) + 999999 * len(colIntersect)
        distances.append(dist)

print(f"Total distance is {sum(distances)}")
