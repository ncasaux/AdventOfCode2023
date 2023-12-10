import aocd

f = aocd.get_data(day=10, year=2023)
scy = scx = ccx = ccy = lineSize = None
maze = []
mazeCells = {}
direction = ""
clockwiseTurnCount = 0.0
leftCells = {}
rightCells = {}


def listEmptyCellsOnLeft(y, x, d):
    if d == "S":
        remaining_length_left = lineSize - x - 1
        for k in range(remaining_length_left):
            if not (y, x + 1 + k) in mazeCells:
                leftCells[(y, x + 1 + k)] = True
            else:
                break
    if d == "N":
        remaining_length_left = x
        for k in range(remaining_length_left):
            if not (y, x - 1 - k) in mazeCells:
                leftCells[(y, x - 1 - k)] = True
            else:
                break


def listEmptyCellsOnRight(y, x, d):
    if d == "S":
        remaining_length_right = x
        for k in range(remaining_length_right):
            if not (y, x - 1 - k) in mazeCells:
                rightCells[(y, x - 1 - k)] = True
            else:
                break
    if d == "N":
        remaining_length_right = lineSize - x - 1
        for k in range(remaining_length_right):
            if not (y, x + 1 + k) in mazeCells:
                rightCells[(y, x + 1 + k)] = True
            else:
                break


for index, currentLine in enumerate(f.splitlines()):
    mazeLine = list(currentLine)
    if "S" in currentLine:
        scy, scx = index, str(currentLine).index("S")
    maze.append(mazeLine)

mazeCells[(scy, scx)] = True

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

lineSize = len(maze[0])
stepCount = 1

while ccy != scy or ccx != scx:
    stepCount += 1
    mazeCells[(ccy, ccx)] = True
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

while ccy != scy or ccx != scx:
    stepCount += 1
    match maze[ccy][ccx]:
        case "|":
            if direction == "S":
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy += 1
            else:
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy -= 1
        case "-":
            if direction == "E":
                ccx += 1
            else:
                ccx -= 1
        case "L":
            if direction == "S":
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                direction = "E"
                ccx += 1
                clockwiseTurnCount -= 0.25
            else:
                direction = "N"
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy -= 1
                clockwiseTurnCount += 0.25
        case "J":
            if direction == "S":
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                direction = "W"
                ccx -= 1
                clockwiseTurnCount += 0.25
            else:
                direction = "N"
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy -= 1
                clockwiseTurnCount -= 0.25
        case "7":
            if direction == "N":
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                direction = "W"
                ccx -= 1
                clockwiseTurnCount -= 0.25
            else:
                direction = "S"
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy += 1
                clockwiseTurnCount += 0.25
        case "F":
            if direction == "N":
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                direction = "E"
                ccx += 1
                clockwiseTurnCount += 0.25
            else:
                direction = "S"
                listEmptyCellsOnLeft(ccy, ccx, direction)
                listEmptyCellsOnRight(ccy, ccx, direction)
                ccy += 1
                clockwiseTurnCount -= 0.25

print(f"Back to starting cell in {stepCount} steps and {clockwiseTurnCount} turns.")

if clockwiseTurnCount > 0:
    print(f"Number of turns was positive, so had to count tiles on the right, which is {len(rightCells)}.")
if clockwiseTurnCount < 0:
    print(f"Number of turns was negative, so had to count tiles on the left, which is {len(leftCells)}.")
