# the magician can to fireball, otrnado, firestorm, mulbok, biba, blizzard
# 4 x 4 격자에서 연습
# (r,c)는 row r, column c
# 격자 왼쪽 위는 (1,1), 오른쪽 아래는 (4,4)
# in the grid there are a total of m fish

# one fish in one box. they can move.
# fish can move 8 ways up, ul ur, r, bl, br, b, l
# shark is in grid too
# fish can overlap each other. the shark can overlap with fish

# Here is how the practice goes
# 1. clone all fish. (takes time so it happens in 5)
# 2. fish move one side. [CLEAR!]
#  condition
#   a) cannot go to shark position
#   b) cannot go out of grid
#   c) 물고기 냄새 있는 칸은 못감
#  fish has direction(predefined)
# their direction changes 45 degrees counter-clockwise until valid
# if no valid, no move
# 3. shark moves consecutively 3 times
#   condition
#   a) shark moves 4 directions. u l r b
#   b) cannot move out of grid
# when fish is "met" while moving, all fish are deleted
# when fish dies, their smell is let.
# the shark moves to places where most fish can be deleted
# (사전순??)
# 상어의 이동방법을 하려면 우선 방향을 정수로 변환 상1, 좌2, 하3, 우4
# 수를 이어 붙여 정수로 하나 만든다.
# 상어는 연속 3번 움직일 수 있기 때문에 3번 움직이는 모든것을 다 나열해야 함
#   condition
#   a) shark cannot move out of grid
#   b) shark chooses path that has most fish count
# Q) 만약 동일한 수의 물고기를 전달하는 루트면???
#   A) 사전순으로 가장 앞서는 방법을 고려
#   즉, 먼저 가능한 모든 루트를 훑으며 물고기 가장 많은 것을 알아낸다
#   좋은 조건의 루트가 여러개이면 그때 사전순으로 하나 선택
# 이동 한번 할때마다 4^3 가진 이동을 다 고려해서. 숫자로 나타내야 한다
# str으로 concatenate

# 4. the smell of fish 2 practices ago are deleted from grid
# 5. fish are cloned at the same place they were born

# Input
# 1) 격자에 있는 물고기의 위치와 방향
# 2) 상어의 위치
# 3) 연습횟수(s번)

# Problem
# s번 연습이 마쳤을 때 격자에 있는 물고기의 수?

# M= 물고기의 수, S=연습횟수
# M은 최대 10마리: 최대 열마리의 물고기 존재
# M은 dict로 관리해도 될듯하다
M, S = map(int, input().split())
# element is [fx, fy, d] # fx, fy is position,
fish_data = [input().split() for _ in range(M)]
fish = []
original_fish = []  # fish는 clone을 위해서 copy 한것
smell = {}
for data in fish_data:
    fx = int(data[0])  # fx is row
    fy = int(data[1])  # fy is column
    d = int(data[2])
    dir = "l"
    if d == 1:
        dir = "l"
    elif d == 2:
        dir = "ul"
    elif d == 3:
        dir = "u"
    elif d == 4:
        dir = "ur"
    elif d == 5:
        dir = "r"
    elif d == 6:
        dir = "br"
    elif d == 7:
        dir = "b"
    elif d == 8:
        dir = "bl"
    fish.append([fx, fy, dir])
    original_fish.append([fx, fy, dir])

shark_x, shark_y = map(int, input().split())
shark = [shark_x, shark_y]  # shark_x is row, shark_y is column

# 격자는 4x4?


def generate_pos_id(fx, fy):
    return f'{fx}_{fy}'


def move_fish(fish, smell: dict, shark):
    # move to direction
    # 3 conditions
    # condition 1: see if is out of grid
    for fish_data in fish:
        r_f = fish_data[0]
        c_f = fish_data[1]
        original_d = fish_data[2]
        d_f = fish_data[2]  # this is string
        is_movable = False
        delta = [0, 0]  # idx 0 is row op idx 1 is col op
        next_d = ""  # counter clockwise op
        cnt = 0
        while is_movable is False:
            # if we have went through all directions
            # we stop searching
            # we do not care for the initial stage
            if d_f == original_d and cnt != 0:
                delta[0] = 0
                delta[1] = 0
                break
            if d_f == "u":
                delta[0] = -1
                delta[1] = 0
                next_d = "ul"
            elif d_f == "ul":
                delta[0] = -1
                delta[1] = -1
                next_d = "l"
            elif d_f == "ur":
                delta[0] = -1
                delta[1] = 1
                next_d = "u"
            elif d_f == "r":
                delta[0] = 0
                delta[1] = 1
                next_d = "ur"
            elif d_f == "l":
                delta[0] = 0
                delta[1] = -1
                next_d = "bl"
            elif d_f == "b":
                delta[0] = 1
                delta[1] = 0
                next_d = "br"
            elif d_f == "bl":
                delta[0] = 1
                delta[1] = -1
                next_d = "b"
            elif d_f == "br":
                delta[0] = 1
                delta[1] = 1
                next_d = "r"
            cnt += 1
            next_r = r_f + delta[0]
            next_c = c_f + delta[1]
            # Condition 1) Check if outside of grid
            if next_r < 1 or next_r > 4:
                delta[0] = 0
                delta[1] = 0
                d_f = next_d
                continue

            if next_c < 1 or next_c > 4:
                delta[0] = 0
                delta[1] = 0
                d_f = next_d
                continue

            # Condition 2) Check if smell is there
            next_pos_id = generate_pos_id(next_r, next_c)
            if smell.get(next_pos_id):
                delta[0] = 0
                delta[1] = 0
                d_f = next_d
                continue

            # Condition 3) Check if shark is there
            if next_r == shark[0] and next_c == shark[1]:
                delta[0] = 0
                delta[1] = 0
                d_f = next_d
                continue

            # if it passes all then the fish can move
            is_movable = True

        # after the while loop
        next_pos = [r_f + delta[0], c_f + delta[1]]
        fish_data[0] = next_pos[0]
        fish_data[1] = next_pos[1]
        # remember fish[2] is direction, and to us it is string
        fish_data[2] = d_f


def dfs_route(route, visited: dict):
    possible = ["1", "2", "3", "4"]
    visited[route] = True
    if len(route) == 3:
        return visited

    for dir in possible:
        new_route = route + dir
        if not visited.get(new_route):
            dfs_route(new_route, visited)


visited = {}
dfs_route("1", visited)  # up
dfs_route("2", visited)  # left
dfs_route("3", visited)  # bottom
dfs_route("4", visited)  # right
seqs = []

for key in visited.keys():
    if len(key) == 3:
        seqs.append(key)


def get_shark_delta(str):
    delta = [0, 0]
    if str == "1":
        delta[0] = -1
        delta[1] = 0
    elif str == "2":
        delta[0] = 0
        delta[1] = -1
    elif str == "3":
        delta[0] = 1
        delta[1] = 0
    elif str == "4":
        delta[0] = 0
        delta[1] = 1
    return delta


def move_shark(fish, pos, seqs, smell):
    # 3 consecutive moves
    # first we look at all possible moves
    # 1:up 2:left 3:bottom 4:right
    # We must run a loop of 4^3
    valid_seqs = {}
    max_fish = 0
    for seq in seqs:
        shark_mov = [0, 0]

        shark_mov[0] = pos[0]
        shark_mov[1] = pos[1]

        step1 = seq[0]
        step2 = seq[1]
        step3 = seq[2]
        step1_delta = get_shark_delta(step1)
        shark_mov[0] += step1_delta[0]
        shark_mov[1] += step1_delta[1]

        dead_fish = 0
        visited = {}

        if shark_mov[0] < 1 or shark_mov[0] > 4 or shark_mov[1] < 1 or shark_mov[1] > 4:
            continue

        # We should count dead fish. However, remember that this indice can be visited
        # only count dead fish if the position was not visited
        mov_1 = generate_pos_id(shark_mov[0], shark_mov[1])
        if not visited.get(mov_1):
            visited[mov_1] = True
            for el in fish:
                fx = el[0]
                fy = el[1]
                if fx == shark_mov[0] and fy == shark_mov[1]:
                    dead_fish += 1

        step2_delta = get_shark_delta(step2)
        shark_mov[0] += step2_delta[0]
        shark_mov[1] += step2_delta[1]

        if shark_mov[0] < 1 or shark_mov[0] > 4 or shark_mov[1] < 1 or shark_mov[1] > 4:
            continue

        mov_2 = generate_pos_id(shark_mov[0], shark_mov[1])
        if not visited.get(mov_2):
            visited[mov_2] = True
            for el in fish:
                fx = el[0]
                fy = el[1]
                if fx == shark_mov[0] and fy == shark_mov[1]:
                    dead_fish += 1

        step3_delta = get_shark_delta(step3)
        shark_mov[0] += step3_delta[0]
        shark_mov[1] += step3_delta[1]

        if shark_mov[0] < 1 or shark_mov[0] > 4 or shark_mov[1] < 1 or shark_mov[1] > 4:
            continue

        mov_3 = generate_pos_id(shark_mov[0], shark_mov[1])
        if not visited.get(mov_3):
            visited[mov_3] = True
            for el in fish:
                fx = el[0]
                fy = el[1]
                if fx == shark_mov[0] and fy == shark_mov[1]:
                    dead_fish += 1

        if dead_fish > max_fish:
            max_fish = dead_fish

        # we record the dead fish count of each seq
        valid_seqs[seq] = dead_fish

    candidates = []
    final_dead = 0
    for key in valid_seqs.keys():
        kill_count = valid_seqs[key]
        if kill_count == max_fish:
            candidates.append(key)

    min_code = 555
    min_code = candidates[0]
    if min_code == 555:
        raise Exception("no routes!")

    final_route = str(min_code)
    left_fish = []
    r1 = final_route[0]
    r1_delta = get_shark_delta(r1)
    pos[0] += r1_delta[0]
    pos[1] += r1_delta[1]
    ignore_fish_idxs = {}
    for i in range(len(fish)):
        el = fish[i]
        fx = el[0]
        fy = el[1]
        d = el[2]
        if fx == pos[0] and fy == pos[1]:
            dead_id = generate_pos_id(fx, fy)
            smell[dead_id] = 0  # first turn
            ignore_fish_idxs[str(i)] = True
            final_dead += 1

    r2 = final_route[1]
    r2_delta = get_shark_delta(r2)
    pos[0] += r2_delta[0]
    pos[1] += r2_delta[1]
    for i in range(len(fish)):
        el = fish[i]
        fx = el[0]
        fy = el[1]
        d = el[2]
        if fx == pos[0] and fy == pos[1]:
            dead_id = generate_pos_id(fx, fy)
            smell[dead_id] = 0  # first turn
            ignore_fish_idxs[str(i)] = True
            final_dead += 1

    r3 = final_route[2]
    r3_delta = get_shark_delta(r3)
    pos[0] += r3_delta[0]
    pos[1] += r3_delta[1]

    for i in range(len(fish)):
        el = fish[i]
        fx = el[0]
        fy = el[1]
        d = el[2]
        if fx == pos[0] and fy == pos[1]:
            dead_id = generate_pos_id(fx, fy)
            smell[dead_id] = 0  # first turn
            ignore_fish_idxs[str(i)] = True
            final_dead += 1

    for i in range(len(fish)):
        if not ignore_fish_idxs.get(str(i)):
            left_fish.append(fish[i])

    return left_fish, final_dead


def update_smell(smell: dict):
    new_smell = {}
    for key in smell.keys():
        smell[key] += 1  # update day
        if smell[key] > 2:
            continue
        else:
            new_smell[key] = smell[key]
    smell = new_smell
    print(smell)


def revive_fish(orig_data, fish):
    for item in orig_data:
        fish.append([item[0], item[1], item[2]])


for t in range(S):
    move_fish(fish, smell, shark)
    left_fish, final_dead = move_shark(fish, shark, seqs, smell)
    fish = left_fish
    update_smell(smell)
    revive_fish(original_fish, fish)
    # print(shark, fish)
    original_fish = []
    for item in fish:
        original_fish.append([item[0], item[1], item[2]])

print(len(fish))
