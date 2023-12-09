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
        pyramid[i].insert(0, pyramid[i][0] - pyramid[i + 1][0])

    totalSum += pyramid[0][0]

print(f"Total sum is {totalSum}.")
