# heater
# make house into grid of R x C (one grid size is 1 x 1)
# R means row and C means column count
# intention: measure the heat of (r,c) where r is row index and c is column index
import math

# 성능 테스트 방법
# 1: all heaters emit wind
# 2: heat is managed
# 3: edge grids (if their heat is over 1 then -1) -> if 0 no decrease
# 4: eat a chocolate (?)
# 5: check if all deisgnated blocks have over K heat!. If yes, then test stops, if no go to step1

# About the heater
# heater can emit wind to either up left bottom right (4 directions)
# if heater emits wind 삼각형 모양으로 각 칸의 온도가 높아진다
# Condition 1 (Algorithm)
# 1 block diff 5 | 2 block diff 4 | 3 block diff 3
# algorithm
# if (x,y) has its heat increased by k, then (x-1, y+1), (x, y + 1), (x+1, y+1) increases heat by k-1
# if there is no block their then the wind does not move
# if multiple wind arrive at a block the heat does not add up together

# Conodition 2 (Wall Presence)
# Check three conditions for wall
# wall presence means or

# Condition 3
# There may be more than 2 heaters
# if there are multiple heaters, then both heat values
# the block where heater is can increase in heat

# How is heat managed?
# For all neighboring blocks, from high to low floor (high - low) / 4
# ex 5, 0 (5/4) = 1.25 -> 1
# subtract 1 by the amount of reachable blocks
# if there are walls between the neighboring blocks, then heat is not transmitted

# +) subtraction in edges
# -1 for all edges. if it is 0, no more subtraction

# you are given: room size, heater position, wall position, and block position for research
# output: eaten chocolate (if chocolate count is over 100 print 101)


# R is Row count C is column count K is condition
R, C, K = map(int, input().split())
# From second line, we are given R lines of the info of room
heat = []  # 2d array
heaters = {}  # we are going to save their positions as key and direction as value
check = []  # store of tuples
walls = {}
chocolate = 0


def gen_pos_id(r, c):
    return f"{r}_{c}"


def parse_pos_id(pos_id):
    splitted = pos_id.split("_")
    r = int(splitted[0])
    c = int(splitted[1])
    return r, c  # return tuple


def gen_wall_pos_id(x1, y1, x2, y2):
    return f"{x1}_{y1}_{x2}_{y2}"


def get_heat(r, c):
    global R
    global C
    global heat
    corr_r = r - 1
    corr_c = c - 1
    if corr_r < 0 or corr_r > R - 1:
        return -1
    if corr_c < 0 or corr_c > C - 1:
        return -1
    return heat[corr_r][corr_c]


def add_heat(array, r, c, value):
    global R
    global C
    corr_r = r - 1
    corr_c = c - 1
    if corr_r < 0 or corr_r > R - 1:
        raise Exception("row index out of bound")
    if corr_c < 0 or corr_c > C - 1:
        raise Exception("column index out of bound")
    array[corr_r][corr_c] += value


def get_delta_for_consider(dir):
    # 부는 방향 입장 첫번째는 ul, 두번째는 u, 세번째는 ur
    if dir == "r":
        return [[-1, 1], [0, 1], [1, 1]]
    elif dir == "l":
        return [[1, -1], [0, -1], [-1, -1]]
    elif dir == "u":
        return [[-1, -1], [-1, 0], [-1, 1]]
    elif dir == "b":
        return [[1, 1], [1, 0], [1, -1]]
    else:
        raise Exception("undefined direction")


def parse_wall_pos_id(wall_pos_id):
    splitted = wall_pos_id.split("_")
    x1 = int(splitted[0])
    y1 = int(splitted[1])
    x2 = int(splitted[2])
    y2 = int(splitted[3])
    return x1, y1, x2, y2


for i in range(R):
    temp = []
    columns = input().split()
    temp_heat = []
    for j in range(len(columns)):
        col_v = columns[j]
        pos_id = gen_pos_id(i + 1, j + 1)
        temp_heat.append(0)
        if col_v == "0":
            # empty block
            continue
        elif col_v == "1":
            # heater to right
            heaters[pos_id] = "r"
        elif col_v == "2":
            # heater to left
            heaters[pos_id] = "l"
        elif col_v == "3":
            # heater to up
            heaters[pos_id] = "u"
        elif col_v == "4":
            # heater to bottom
            heaters[pos_id] = "b"
        elif col_v == "5":
            check.append((i + 1, j + 1))  # tuple

    heat.append(temp_heat)

W = int(input())

for i in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        wall_pos_id1 = gen_wall_pos_id(x, y, x - 1, y)
        wall_pos_id2 = gen_wall_pos_id(x - 1, y, x, y)
        walls[wall_pos_id1] = True
        walls[wall_pos_id2] = True
        # wall is between x,y and x-1, y
    elif t == 1:
        # wall is between x,y and x, y+1
        wall_pos_id1 = gen_wall_pos_id(x, y, x, y + 1)
        wall_pos_id2 = gen_wall_pos_id(x, y + 1, x, y)
        walls[wall_pos_id1] = True
        walls[wall_pos_id2] = True


def emit_wind():
    global heaters
    global heat
    global walls
    global R
    global C

    # bfs
    for heater_id in heaters.keys():
        visited = {}
        heater_x, heater_y = parse_pos_id(heater_id)
        dir = heaters[heater_id]  # dir is either r l u b
        queue = []
        if dir == "r":
            queue.append([heater_x, heater_y + 1])
        elif dir == "l":
            queue.append([heater_x, heater_y - 1])
        elif dir == "u":
            queue.append([heater_x - 1, heater_y])
        elif dir == "b":
            queue.append([heater_x + 1, heater_y])

        initial_id = gen_pos_id(queue[0][0], queue[0][1])
        visited[initial_id] = 5  # this has value of adding
        add_heat(heat, queue[0][0], queue[0][1], 5)
        deltas = get_delta_for_consider(dir)
        while len(queue) > 0:
            # in the eyes of the wind, we should look up left, up, up right
            item = queue.pop()
            item_id = gen_pos_id(item[0], item[1])
            heat_origin = visited.get(item_id)
            if heat_origin is None:
                raise Exception("visited has no info")

            for k in range(len(deltas)):
                delta = deltas[k]
                next_x, next_y = item[0] + delta[0], item[1] + delta[1]
                next_id = gen_pos_id(next_x, next_y)
                # 1. first check out of bound
                if next_x < 1 or next_x > R:
                    continue
                if next_y < 1 or next_y > C:
                    continue

                # 2. second check if visited
                if visited.get(next_id) is not None:
                    continue

                # 3. third check wall
                # 3-1. check up left
                if k == 0:
                    inter_x, inter_y = -1, -1
                    if dir == "r":
                        inter_x, inter_y = item[0] - 1, item[1]  # u
                    elif dir == "l":
                        inter_x, inter_y = item[0] + 1, item[1]  # b
                    elif dir == "u":
                        inter_x, inter_y = item[0], item[1] - 1  # l
                    elif dir == "b":
                        inter_x, inter_y = item[0], item[1] + 1  # r
                    # check wall between item and inter
                    temp_wall_id1 = gen_wall_pos_id(item[0], item[1], inter_x, inter_y)
                    if walls.get(temp_wall_id1) is not None:
                        continue
                    # check wall between next pos and inter
                    temp_wall_id2 = gen_wall_pos_id(next_x, next_y, inter_x, inter_y)
                    if walls.get(temp_wall_id2) is not None:
                        continue
                elif k == 1:
                    # check wall between item and next pos
                    temp_wall_id1 = gen_wall_pos_id(item[0], item[1], next_x, next_y)
                    if walls.get(temp_wall_id1) is not None:
                        continue

                elif k == 2:
                    inter_x, inter_y = -1, -1
                    if dir == "r":
                        inter_x, inter_y = item[0] + 1, item[1]  # u
                    elif dir == "l":
                        inter_x, inter_y = item[0] - 1, item[1]  # b
                    elif dir == "u":
                        inter_x, inter_y = item[0], item[1] + 1  # l
                    elif dir == "b":
                        inter_x, inter_y = item[0], item[1] - 1  # r
                    # check wall between item and inter
                    temp_wall_id1 = gen_wall_pos_id(item[0], item[1], inter_x, inter_y)
                    if walls.get(temp_wall_id1) is not None:
                        continue
                    # check wall between next pos and inter
                    temp_wall_id2 = gen_wall_pos_id(next_x, next_y, inter_x, inter_y)
                    if walls.get(temp_wall_id2) is not None:
                        continue
                # for next_pos that has succesfully went through the conditions, we record in visited and we add to queue
                visited[next_id] = heat_origin - 1  #
                if heat_origin - 1 >= 1:
                    queue.append([next_x, next_y])
                    add_heat(heat, next_x, next_y, heat_origin - 1)

def share_heat():
    global heaters
    global heat
    global walls
    global R
    global C

    new_heat = []
    # we share heat for four directions u l r b
    temp_heat = []
    for i in range(R):
        temp_row = []
        for j in range(C):
            temp_row.append(heat[i][j])
        temp_heat.append(temp_row)

    for i in range(R):
        for j in range(C):
            r = i + 1
            c = j + 1
            heat_value = get_heat(r, c)
            total_subtract = 0
            # 1. check if out bound
            # 2. check if big (then proceed share)
            # 3. check if wall exists
            u_x, u_y = r - 1, c
            u_value = get_heat(u_x, u_y)
            wall_u_id = gen_wall_pos_id(r,c, u_x, u_y)
            wall_u = walls.get(wall_u_id)
            if u_value != -1:
                if heat_value > u_value and wall_u is None:
                    amount = math.floor((heat_value - u_value)/4)
                    add_heat(temp_heat, u_x, u_y, amount)
                    total_subtract += amount

            b_x, b_y = r + 1, c
            b_value = get_heat(b_x, b_y)
            wall_b_id = gen_wall_pos_id(r,c,b_x,b_y)
            wall_b = walls.get(wall_b_id)
            if b_value != -1:
                if heat_value > b_value and wall_b is None:
                    amount = math.floor((heat_value - b_value)/4)
                    add_heat(temp_heat, b_x, b_y, amount)
                    total_subtract += amount

            r_x, r_y = r, c+1
            r_value = get_heat(r_x, r_y)
            wall_r_id = gen_wall_pos_id(r,c,r_x,r_y)
            wall_r = walls.get(wall_r_id)
            if r_value != -1:
                if heat_value > r_value and wall_r is None:
                    amount = math.floor((heat_value - r_value)/4)
                    add_heat(temp_heat, r_x, r_y, amount)
                    total_subtract += amount

            l_x, l_y = r, c-1
            l_value = get_heat(l_x, l_y)
            wall_l_id = gen_wall_pos_id(r,c,l_x,l_y)
            wall_l = walls.get(wall_l_id)
            if l_value != -1:
                if heat_value > l_value and wall_l is None:
                    amount = math.floor((heat_value - l_value)/4)
                    add_heat(temp_heat, l_x, l_y, amount)
                    total_subtract += amount

            add_heat(temp_heat, r, c, -total_subtract)
    heat = temp_heat

def remove_edges():
    global heat
    global C
    global R

    for i in range(C):
        if heat[0][i] > 0:
            heat[0][i] -= 1
        if heat[R-1][i] > 0:
            heat[R-1][i] -= 1

    for i in range(R):
        if i == 0:
            continue
        elif i == R - 1:
            continue
        if heat[i][0] > 0:
            heat[i][0] -= 1
        if heat[i][C-1] > 0:
            heat[i][C-1] -= 1

while chocolate <= 100:
    emit_wind()
    share_heat()
    remove_edges()
    chocolate += 1
    is_valid = True
    for i in range(len(check)):
        r, c = check[i]
        check_value = get_heat(r, c)
        if check_value == -1:
            raise Exception("check value not found")
        if check_value < K:
            is_valid = False
            break
    if is_valid:
        break


print(chocolate)