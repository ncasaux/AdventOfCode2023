import aocd
import re
from collections import defaultdict

f = aocd.get_data(day=5, year=2023)
f = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def calculate_range_and_diff(mapping):
    mapping_list = []
    for j in mapping:
        min_value = j[1]
        max_value = j[1] + j[2] - 1
        diff = j[0] - j[1]
        mapping_list.append([min_value, max_value, range(min_value, max_value + 1), diff])
    mapping_list.sort()
    return mapping_list


locations = []
seedRangeTuples = []
almanach = defaultdict(list)
mappingTypes = ["seed-to-soil", "soil-to-fertilizer", "fertilizer-to-water", "water-to-light", "light-to-temperature",
                "temperature-to-humidity", "humidity-to-location"]

matches = re.findall(r"seeds:(.*)\n\n", f, re.MULTILINE)
seeds = [int(i) for i in matches[0].split()]

for mt in mappingTypes:
    matches = re.findall(mt + r" map:((?:\n[\d ]*)*)", f, re.MULTILINE)
    mappingList = [[int(j) for j in i.split()] for i in matches[0].rstrip().lstrip().split("\n")]
    almanach[mt] = calculate_range_and_diff(mappingList)

for c in range(0, len(seeds), 2):
    seedRangeTuples.append((seeds[c], seeds[c] + seeds[c + 1] - 1))

for s in seedRangeTuples:
    srcSrt = [s]

    tgtSrt = []
    for mt in mappingTypes:
        for srt in srcSrt:
            for almanachRange in almanach[mt]:
                print(f"Processing seed range {srt} against {mt} mapping and {almanachRange}.")
                if srt[0] < almanachRange[0] and srt[1] < almanachRange[0]:
                    tgtSrt.append(srt)
                elif srt[0] > almanachRange[1] and srt[1] > almanachRange[1]:
                    tgtSrt.append(srt)
                elif srt[0] < almanachRange[0] and srt[1] in almanachRange[2]:
                    tgtSrt.append((srt[0], almanachRange[0] - 1))
                    tgtSrt.append((almanachRange[0] + almanachRange[3], srt[1] + almanachRange[3]))
                elif srt[0] in almanachRange[2] and srt[1] > almanachRange[1]:
                    tgtSrt.append((srt[0] + almanachRange[3], almanachRange[1] + almanachRange[3]))
                    tgtSrt.append((almanachRange[1] + 1, srt[1]))
                elif srt[0] in almanachRange[2] and srt[1] in almanachRange[2]:
                    tgtSrt.append((srt[0] + almanachRange[3], srt[1] + almanachRange[3]))
                print(f"Transformed to {tgtSrt}.")
        srcSrt = tgtSrt

for s in seeds:
    for mt in mappingTypes:
        for r in almanach[mt]:
            if s in r:
                s += almanach[mt][r]
                break
    locations.append(s)

print(f"Lowest location is {min(locations)}.")
