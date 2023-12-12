import aocd
import re

f = aocd.get_data(day=12, year=2023)
f = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

validCombination = []


def addValidCombination(begin, end, pattern):
    if len(end) > 0:
        if end[0] == "?":
            addValidCombination(begin + "#", end[1:], pattern)
            addValidCombination(begin + ".", end[1:], pattern)
        elif end[0] == "#" or  end[0] == ".":
            addValidCombination(begin + end[0], end[1:], pattern)
    else:
        regex = r"^\.*#{" + str(pattern).replace(",","}\\.+#{") + r"}\.*$"
        print(f"Testing {begin}. against {regex}")
        match = re.search(regex,begin)
        if match is not None: validCombination.append(begin)


for rowIndex, currentLine in enumerate(f.splitlines()):
    s, p =  str(currentLine).split(" ")
    addValidCombination("", s+"?"+s+"?"+s+"?"+s+"?"+s, p+","+p+","+p+","+p+","+p)

print(len(validCombination))

