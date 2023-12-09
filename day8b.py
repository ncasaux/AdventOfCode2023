import math
import aocd

f = aocd.get_data(day=8, year=2023)

instructions = f.splitlines()[0]
network = {}
locations = []
for currentLine in f.splitlines()[2:]:
    src = currentLine.replace(" ", "").split("=")[0]
    if src.endswith("A"):
        locations.append(src)
    dst = tuple(currentLine.replace(" ", "").split("=")[1][1:-1].split(","))
    network[src] = dst

stepsList = []
for index, location in enumerate(locations):
    steps = 0
    while not str(location).endswith("Z") :
        instruction = instructions[steps % len(instructions)]
        if instruction == "R":
            location = network[location][1]
        elif instruction == "L":
            location = network[location][0]
        steps += 1
    stepsList.append(steps)

print(f"Reached all '**Z' locations in {math.lcm(*stepsList)} steps.")
