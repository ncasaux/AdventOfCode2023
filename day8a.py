import aocd

f = aocd.get_data(day=8, year=2023)

instructions = f.splitlines()[0]
network = {}
for currentLine in f.splitlines()[2:]:
    src = currentLine.replace(" ", "").split("=")[0]
    dst = tuple(currentLine.replace(" ", "").split("=")[1][1:-1].split(","))
    network[src] = dst

location = "AAA"
steps = 0
while location != "ZZZ":
    instruction =  instructions[steps % len(instructions)]
    if instruction == "R":
        location = network[location][1]
    elif instruction == "L":
        location = network[location][0]
    steps +=1

print(f"Reached 'ZZZ' in {steps} steps.")
