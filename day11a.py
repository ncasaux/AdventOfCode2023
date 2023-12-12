import aocd

f = aocd.get_data(day=11, year=2023)

rowIndex = colIndex = None
galaxies = []
distances = []

for rowIndex, currentLine in enumerate(f.splitlines()):
    for colIndex, currentChar in enumerate(currentLine):
        if currentChar == "#":
            galaxies.append((rowIndex, colIndex))

galaxiesRow = set([galaxy[0] for galaxy in galaxies])
galaxiesCol = set([galaxy[1] for galaxy in galaxies])

emptyRow = galaxiesRow.symmetric_difference(range(rowIndex + 1))
emptyCol = galaxiesCol.symmetric_difference(range(colIndex + 1))

for g in range(len(galaxies)):
    for h in range(g + 1, len(galaxies)):
        rowIntersect = emptyRow.intersection(
            range(min(galaxies[g][0], galaxies[h][0]), max(galaxies[g][0], galaxies[h][0])))
        colIntersect = emptyCol.intersection(
            range(min(galaxies[g][1], galaxies[h][1]), max(galaxies[g][1], galaxies[h][1])))
        dist = abs(galaxies[h][0] - galaxies[g][0]) + len(rowIntersect) + abs(galaxies[h][1] - galaxies[g][1]) + len(
            colIntersect)
        # print(f"Distance between {g+1} and {h+1} is {dist}.")
        distances.append(dist)

print(f"Total distance is {sum(distances)}")
