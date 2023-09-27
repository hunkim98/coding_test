import copy

fishSmell = [list([0] * 4) for i in range(4)]
d_x = [0, -1, -1, -1, 0, 1, 1, 1]
d_y = [-1, -1, 0, 1, 1, 1, 0, -1]


def sharkMove(s_x, s_y, plate):
    queue = [(s_x, s_y, 0, "")]
    dd_x = [-1, 0, 1, 0]
    dd_y = [0, -1, 0, 1]
    maxEatNum = -1
    pathList = []

    for i in range(4):
        for j in range(4):
            for k in range(4):
                addedEatNum = 0
                pathPointList = []
                n_x = s_x + dd_x[i]
                n_y = s_y + dd_y[i]

                if 0 <= n_x and n_x < 4 and 0 <= n_y and n_y < 4:
                    boxFishNum = 0
                    for fishNum in plate[n_x][n_y].values():
                        boxFishNum += fishNum
                    addedEatNum += boxFishNum
                    pathPointList.append([n_x, n_y, boxFishNum])
                else:
                    continue

                n_x = n_x + dd_x[j]
                n_y = n_y + dd_y[j]

                if 0 <= n_x and n_x < 4 and 0 <= n_y and n_y < 4:
                    boxFishNum = 0
                    if [n_x, n_y] not in [[nx, ny] for nx, ny, _ in pathPointList]:
                        for fishNum in plate[n_x][n_y].values():
                            boxFishNum += fishNum
                    addedEatNum += boxFishNum
                    pathPointList.append([n_x, n_y, boxFishNum])
                else:
                    continue

                n_x = n_x + dd_x[k]
                n_y = n_y + dd_y[k]

                if 0 <= n_x and n_x < 4 and 0 <= n_y and n_y < 4:
                    boxFishNum = 0
                    if [n_x, n_y] not in [[nx, ny] for nx, ny, _ in pathPointList]:
                        for fishNum in plate[n_x][n_y].values():
                            boxFishNum += fishNum
                    addedEatNum += boxFishNum
                    pathPointList.append([n_x, n_y, boxFishNum])
                else:
                    continue

                if maxEatNum < addedEatNum:
                    maxEatNum = addedEatNum
                    pathList = pathPointList
    return pathList


def process(s_x, s_y, plate):
    global fishSmell
    global d_x
    global d_y

    save = copy.deepcopy(plate)

    for x in range(4):
        for y in range(4):
            for firstDirection, numOfFish in save[x][y].items():
                count = 0
                d = firstDirection

                while count < 8:
                    n_x = x + d_x[d]
                    n_y = y + d_y[d]

                    if 0 <= n_x and n_x < 4 and 0 <= n_y and n_y < 4 and fishSmell[n_x][n_y] == 0 and [n_x, n_y] != [s_x, s_y]:
                        if d not in plate[n_x][n_y]:
                            plate[n_x][n_y][d] = numOfFish
                        else:
                            plate[n_x][n_y][d] += numOfFish
                        plate[x][y][firstDirection] -= numOfFish
                        break

                    d = d - 1 if d - 1 >= 0 else 7
                    count += 1
    pathList = sharkMove(s_x, s_y, plate)
    [s_x, s_y, _] = pathList[-1]
    for x, y, fishNum in pathList:
        plate[x][y] = dict()
        if fishNum > 0:
            fishSmell[x][y] = 3
    for i in range(4):
        for j in range(4):
            if fishSmell[i][j] > 0:
                fishSmell[i][j] -= 1
            for d, numOfFish in save[i][j].items():
                if d not in plate[i][j]:
                    plate[i][j][d] = save[i][j][d]
                else:
                    plate[i][j][d] += save[i][j][d]

    smells = {}
    row = 1
    for smell in fishSmell:
        col = 1
        for item in smell:
            if item:
                smells[f'{row}_{col}'] = True
            col += 1
        row += 1
    print(smells)
    smells.keys()
    return s_x, s_y, plate


plate = [[dict(), dict(), dict(), dict()] for i in range(4)]

M, S = map(int, input().split())

for i in range(M):
    x, y, d = map(int, input().split())
    if d not in plate[x-1][y-1]:
        plate[x-1][y-1][d-1] = 1
    else:
        plate[x-1][y-1][d-1] += 1

s_x, s_y = map(int, input().split())
s_x -= 1
s_y -= 1

for i in range(S):
    s_x, s_y, plate = process(s_x, s_y, plate)

total = 0
for i in range(4):
    for j in range(4):
        for fishNum in plate[i][j].values():
            total += fishNum

print(total)
