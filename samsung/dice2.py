# map size is N and M. right is east, up is north
# map indices is (r,c) r is distance from north and c is distance from west
# top left is (1,1), bottom right is (N,M)
# in the map a dice is positioned
# on the dice there are 1~6 integers
# one side of dice is the same with map
#   2
# 4 1 3
#   5
#   6
# dice state: up is 1 east is 3 (location is top left: (1,1))
# dice first moves to east(right)

# Conditions
# 1. roll once to the move direction
# 2. if there is not valid place, then roll to the opposite direction
# 3. the number(A) beneath the dice decides the next direction of the dice compared with the number in (r,c) (B)
#       if A > B: direction moves clockwise (North -> East)
#       if A < B: direction moves counter-clockwise (North -> West)
#       if A = B: direction is maintained

# Q. What is the score in (r,c)?
# A. Lets say the number in (r,c) is B.
# Starting from (r,c) find the number of valid blocks (C) that we can go.
# Condition: the visited (r + alpha,c + alpha) should have the same integer as the integer in (r,c)
# Now the score is B x C

# N is row size M is column size and K is turns

N, M, K = map(int, input().split())
integers = []
dice_pos = [1, 1]
dice_up_int = 1
dice_bottom_int = 6
dice_int = {
    "top": 1,
    "east": 3,
    "south": 5,
    "bottom": 6,
    "west": 4,
    "north": 2
}


def roll_dice(dir):
    global dice_int
    # there are four directions
    top = dice_int["top"]
    east = dice_int["east"]
    south = dice_int["south"]
    bottom = dice_int["bottom"]
    west = dice_int["west"]
    north = dice_int["north"]
    if dir == "north":
        # 위로 굴린다
        # east, west 는 고정
        dice_int["north"] = top
        dice_int["top"] = south
        dice_int["south"] = bottom
        dice_int["bottom"] = north
    elif dir == "east":
        # 오른쪽으로 굴린다
        # north, south 는 고정
        dice_int["east"] = top
        dice_int["top"] = west
        dice_int["west"] = bottom
        dice_int["bottom"] = east
    elif dir == "south":
        # 아래로 굴린다
        # east, west 는 고정
        dice_int["south"] = top
        dice_int["top"] = north
        dice_int["north"] = bottom
        dice_int["bottom"] = south
    elif dir == "west":
        # 왼쪽으로 굴린다
        # north, south는 고정
        dice_int["west"] = top
        dice_int["top"] = east
        dice_int["east"] = bottom
        dice_int["bottom"] = west
    else:
        raise Exception("undefined direction")


for i in range(N):
    values = [int(k) for k in input().split()]
    integers.append(values)


def get_int(r, c):
    global integers
    global N
    global M
    if r < 1 or r > N:
        return -1  # the integers are all natural numbers
    if c < 1 or c > M:
        return -1
    row_idx = r - 1
    col_idx = c - 1
    return integers[row_idx][col_idx]


def get_next_rotate(is_clockwise, dir):
    final_dir = dir
    if is_clockwise:
        if dir == "north":
            final_dir = "east"
        elif dir == "east":
            final_dir = "south"
        elif dir == "south":
            final_dir = "west"
        elif dir == "west":
            final_dir = "north"
        else:
            raise Exception("Nonexistent direction")
    else:
        if dir == "north":
            final_dir = "west"
        elif dir == "west":
            final_dir = "south"
        elif dir == "south":
            final_dir = "east"
        elif dir == "east":
            final_dir = "north"
        else:
            raise Exception("Nonexistent direction")
    return final_dir


def get_opp_rotate(dir):
    final_dir = dir
    if dir == "north":
        final_dir = "south"
    elif dir == "east":
        final_dir = "west"
    elif dir == "south":
        final_dir = "north"
    elif dir == "west":
        final_dir = "east"
    else:
        raise Exception("Nonexistent direction")
    return final_dir


def get_delta(dir):
    delta = [0, 0]
    if dir == "north":
        delta = [-1, 0]
    elif dir == "east":
        delta = [0, 1]
    elif dir == "south":
        delta = [1, 0]
    elif dir == "west":
        delta = [0, -1]
    else:
        raise Exception("Nonexistent direction")
    return delta


def dfs(visited: dict, pos, integer, new_dir):
    # DFS continue conditions
    delta = get_delta(new_dir)
    new_pos = [pos[0] + delta[0], pos[1] + delta[1]]
    pos_integer = get_int(new_pos[0], new_pos[1])
    if integer != pos_integer:
        # if the integer is not same with pos integer we abort exploring
        return

    pos_id = gen_id(new_pos[0], new_pos[1])
    if visited.get(pos_id):
        return
    visited[pos_id] = True
    dirs = ["north", "east", "south", "west"]
    for explore in dirs:
        dfs(visited, new_pos, integer, explore)


def gen_id(r, c):
    return f"{r}_{c}"


def get_score(B):
    global dice_pos
    visited = {}
    # this does a dfs on the map to find same integers
    curr_id = gen_id(dice_pos[0], dice_pos[1])
    visited[curr_id] = True
    dfs(visited, [dice_pos[0], dice_pos[1]], B, "north")
    dfs(visited, [dice_pos[0], dice_pos[1]], B, "east")
    dfs(visited, [dice_pos[0], dice_pos[1]], B, "south")
    dfs(visited, [dice_pos[0], dice_pos[1]], B, "west")
    C = len(visited.keys())
    # print(visited.keys())
    visited = {}  # initialize\
    return B * C


# first move is east
roll_dir = "east"

total_score = 0

for i in range(K):
    # Step 1 lets rotate the dice
    # but first lets check if there is a block
    final_roll_dir = roll_dir
    delta = get_delta(roll_dir)
    next_pos = [dice_pos[0] + delta[0], dice_pos[1] + delta[1]]
    # B is the int for the row index and column index
    B = get_int(next_pos[0], next_pos[1])
    # -1 means that the dir is not valid
    if B == -1:
        opp_dir = get_opp_rotate(roll_dir)
        final_roll_dir = opp_dir
        delta = get_delta(opp_dir)
        next_pos = [dice_pos[0] + delta[0], dice_pos[1] + delta[1]]
        B = get_int(next_pos[0], next_pos[1])

    roll_dice(final_roll_dir)  # we finally roll the dice with a correct one
    roll_dir = final_roll_dir  # set the roll direction to correct one

    # get value in map, get bottom value in dice
    A = dice_int["bottom"]
    next_roll_dir = roll_dir

    dice_pos[0] = next_pos[0]
    dice_pos[1] = next_pos[1]
    # print(roll_dir)
    # print(dice_pos)
    # print('bottom: ', A)
    # print("map vlaue", B)
    if A > B:
        next_roll_dir = get_next_rotate(is_clockwise=True, dir=roll_dir)
    elif A < B:
        next_roll_dir = get_next_rotate(is_clockwise=False, dir=roll_dir)
    else:  # A==B
        next_roll_dir = roll_dir

    roll_dir = next_roll_dir
    # print("A: ", A, "B: ", B)
    score = get_score(B)
    # print(score)
    total_score += score

print(total_score)
