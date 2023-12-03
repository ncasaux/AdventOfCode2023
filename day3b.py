import aocd
import re
from collections import defaultdict

f = re.sub(r'^.*$', '.\\g<0>.', aocd.get_data(day=3, year=2023), 0, re.MULTILINE)
gearRatioSum = 0
gears = defaultdict(list)

for index, currentLine in enumerate(f.splitlines()):
    for currentMatch in re.finditer("(\\d+)", currentLine):
        leftCharIndex = currentMatch.regs[0][0]
        rightCharIndex = currentMatch.regs[0][-1]

        if index > 0:
            previousLine = f.splitlines()[index - 1]
            previousLineAdjacentChars = previousLine[leftCharIndex - 1:rightCharIndex + 1]
            if previousLineAdjacentChars.find("*") >= 0:
                gear = (index - 1, previousLineAdjacentChars.find("*") + leftCharIndex - 1)
                gears[gear].append(int(currentMatch.group(0)))

        if index < len(f.splitlines()) - 1:
            nextLine = f.splitlines()[index + 1]
            nextLineAdjacentChars = nextLine[leftCharIndex - 1:rightCharIndex + 1]
            if nextLineAdjacentChars.find("*") >= 0:
                gear = (index + 1, nextLineAdjacentChars.find("*") + leftCharIndex - 1)
                gears[gear].append(int(currentMatch.group(0)))

        leftAdjacentChar = currentLine[leftCharIndex - 1:leftCharIndex]
        if leftAdjacentChar == "*":
            gear = (index, leftCharIndex - 1)
            gears[gear].append(int(currentMatch.group(0)))

        rightAdjacentChar = currentLine[rightCharIndex:rightCharIndex + 1]
        if rightAdjacentChar == "*":
            gear = (index, rightCharIndex)
            gears[gear].append(int(currentMatch.group(0)))

for gear, ratio in gears.items():
    if len(ratio) > 1:
        gearRatioSum += ratio[0] * ratio[1]

print(f"Sum of part numbers is {gearRatioSum}.")
