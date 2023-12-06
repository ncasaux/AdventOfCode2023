import aocd

f = aocd.get_data(day=6, year=2023)

raceDurations = [int(i) for i in f.splitlines()[0][5:].lstrip().split()]
recordDistances = [int(i) for i in f.splitlines()[1][9:].lstrip().split()]
record = 1

for raceIndex, raceDuration in enumerate(raceDurations):
    achievedDistances = []
    for d in range(0, raceDuration + 1):
        distance = d * (raceDuration - d)
        achievedDistances.append(distance)

    record *= sum(d > recordDistances[raceIndex] for d in achievedDistances)

print(f"Record is {record}.")
