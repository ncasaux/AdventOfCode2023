import aocd
import re
from collections import defaultdict

f = aocd.get_data(day=4, year=2023)
scratchcards = defaultdict(int)

for index, currentLine in enumerate(f.splitlines(), start=1):
    matches = re.findall(r":(.*)\|(.*)", currentLine, re.MULTILINE)
    left = str(matches[0][0]).strip().split()
    right = str(matches[0][1]).strip().split()
    common = set(left).intersection(right)
    matchingNumber = len(common)

    scratchcards[index] += 1
    for k in range(0, scratchcards[index]):
        for i in range(1, matchingNumber + 1):
            scratchcards[index + i] += 1

print(f"Total number of scratchcards is {sum(scratchcards.values())}.")
