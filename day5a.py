import aocd
import re
from collections import defaultdict

f = aocd.get_data(day=5, year=2023)


def calculateRangeAndDiff(mapping):
    mapping_dict = defaultdict(int)
    for j in mapping:
        min_value = j[1]
        max_value = j[1] + j[2]
        diff = j[0] - j[1]
        mapping_dict[range(min_value, max_value)] = diff
    return mapping_dict


locations = []
mainDict = defaultdict(dict)
mappingTypes = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature",
                "temperature-to-humidity", "humidity-to-location"]

matches = re.findall(r"seeds:(.*)\n\n", f, re.MULTILINE)
seeds = [int(i) for i in matches[0].split()]

for m in mappingTypes:
    matches = re.findall(m + r" map:((?:\n[\d ]*)*)", f, re.MULTILINE)
    mappingList = [[int(j) for j in i.split()] for i in matches[0].rstrip().lstrip().split("\n")]
    mainDict[m] = calculateRangeAndDiff(mappingList)

for s in seeds:
    for m in mappingTypes:
        for r in mainDict[m]:
            if s in r:
                s += mainDict[m][r]
                break
    locations.append(s)

print(f"Lowest location is {min(locations)}.")
