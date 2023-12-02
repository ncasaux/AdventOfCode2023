import aocd
import re

f = aocd.get_data(day=2, year=2023)
validGames = []
gamesPower = []

for index, currentLine,  in enumerate(f.splitlines(), start=1):
    redRegEx = re.findall("(\\d+)\\sred", currentLine)
    redMax = max(map(int,redRegEx))

    blueRegEx = re.findall("(\\d+)\\sblue", currentLine)
    blueMax = max(map(int,blueRegEx))

    greenRegEx = re.findall("(\\d+)\\sgreen", currentLine)
    greenMax = max(map(int,greenRegEx))

    if redMax <= 12 and greenMax <= 13 and blueMax <= 14:
        validGames.append(index)

    gamesPower.append(redMax * greenMax * blueMax)

print(f"Sum of valid games is {sum(validGames)}.")
print(f"Sum of games power {sum(gamesPower)}.")

