import math
import aocd
import re

f = aocd.get_data(day=4, year=2023)
score = 0

for index, currentLine in enumerate(f.splitlines()):
    matches = re.findall(r":(.*)\|(.*)", currentLine, re.MULTILINE)
    left = str(matches[0][0]).strip().split()
    right = str(matches[0][1]).strip().split()
    common = set(left).intersection(right)
    score += int(math.pow(2, len(common) - 1))

print(f"Total points is {score}.")
