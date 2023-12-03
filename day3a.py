import aocd
import re

f = re.sub(r'^.*$', '.\\g<0>.', aocd.get_data(day=3, year=2023), 0, re.MULTILINE)
partNumbers = []

for index, currentLine in enumerate(f.splitlines()):
    for currentMatch in re.finditer("(\\d+)", currentLine):
        leftCharIndex = currentMatch.regs[0][0]
        rightCharIndex = currentMatch.regs[0][-1]
        adjacentChars = ""

        if index > 0:
            previousLine = f.splitlines()[index - 1]
            adjacentChars += previousLine[leftCharIndex - 1:rightCharIndex + 1]

        if index < len(f.splitlines()) - 1:
            nextLine = f.splitlines()[index + 1]
            adjacentChars += nextLine[leftCharIndex - 1:rightCharIndex + 1]

        adjacentChars += currentLine[leftCharIndex - 1:leftCharIndex]
        adjacentChars += currentLine[rightCharIndex:rightCharIndex + 1]

        if len(adjacentChars.replace(".", "")) != 0:
            partNumbers.append(int(currentMatch.group(0)))

print(f"Sum of part numbers is {sum(partNumbers)}.")
