import aocd

f = aocd.get_data(day=10, year=2023)

scy = scx = ccx = ccy = None
maze = []
direction = ""

for index, currentLine in enumerate(f.splitlines()):
    mazeLine = list(currentLine)
    if "S" in currentLine:
        scy, scx = index, str(currentLine).index("S")
    maze.append(mazeLine)

if maze[scy - 1][scx] in ("|", "7", "F"):
    direction = "N"
    ccy, ccx = scy - 1, scx
elif maze[scy + 1][scx] in ("|", "J", "L"):
    direction = "S"
    ccy, ccx = scy + 1, scx
elif maze[scy][scx - 1] in ("-", "F", "L"):
    direction = "E"
    ccy, ccx = scy, scx - 1
elif maze[scy][scx + 1] in ("-", "7", "J"):
    direction = "W"
    ccy, ccx = scy, scx + 1

stepCount = 1
while ccy != scy or ccx != scx:
    stepCount += 1
    match maze[ccy][ccx]:
        case "|":
            if direction == "S":
                ccy += 1
            else:
                ccy -= 1
        case "-":
            if direction == "E":
                ccx += 1
            else:
                ccx -= 1
        case "L":
            if direction == "S":
                ccx += 1
                direction = "E"
            else:
                ccy -= 1
                direction = "N"
        case "J":
            if direction == "S":
                ccx -= 1
                direction = "W"
            else:
                ccy -= 1
                direction = "N"
        case "7":
            if direction == "N":
                ccx -= 1
                direction = "W"
            else:
                ccy += 1
                direction = "S"
        case "F":
            if direction == "N":
                ccx += 1
                direction = "E"
            else:
                ccy += 1
                direction = "S"

print(f"Back to starting cell in {stepCount} steps, so farthest cell is {int(stepCount / 2)} steps away.")
