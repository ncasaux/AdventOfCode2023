import aocd

f = aocd.get_data(day=9, year=2023)
totalSum = 0

for currentLine in f.splitlines():
    integerList = [eval(i) for i in currentLine.split()]
    pyramid = [integerList]
    depth = 0

    while not all(i == 0 for i in pyramid[-1]):
        newList = []
        for i in range(len(pyramid[-1]) - 1):
            newList.append(pyramid[-1][i + 1] - pyramid[-1][i])
        pyramid.append(newList)
        depth += 1

    for i in reversed(range(depth)):
        pyramid[i].append(pyramid[i][-1] + pyramid[i + 1][-1])

    totalSum += pyramid[0][-1]

print(f"Total sum is {totalSum}.")
