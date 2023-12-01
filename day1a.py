import aocd
import re

f = aocd.get_data(day=1, year=2023)
calibrationValue: int = 0

for currentLine in f.splitlines():
    r = re.findall("(\\d{1})", currentLine)
    calibrationValue += int(r[0])*10 + int(r[-1])

print(f"Sum of all calibration value is {calibrationValue}.")