import aocd
import re

f = aocd.get_data(day=1, year=2023)
calibrationValue: int = 0

mapping: dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

for currentLine in f.splitlines():
    firstCalibrationRegEx = re.findall("(\\d{1}|one|two|three|four|five|six|seven|eight|nine)", currentLine)
    firstCalibrationValue = int(mapping.get(firstCalibrationRegEx[0],firstCalibrationRegEx[0]))

    lastCalibrationRegEx = re.findall(".*(\\d{1}|one|two|three|four|five|six|seven|eight|nine)", currentLine)
    lastCalibrationValue = int(mapping.get(lastCalibrationRegEx[0],lastCalibrationRegEx[0]))

    currentLineCalibrationValue = 10 * firstCalibrationValue + lastCalibrationValue
    calibrationValue += currentLineCalibrationValue

print(f"Sum of all calibration values is {calibrationValue}.")