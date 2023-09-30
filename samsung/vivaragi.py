# Grid is N, N
# one baguni is 1x1
# one baguni can have unlimited amount of water
# (r,c) r = row, c = column. A[r][c] is the amount of water in baguni (r,c)
# top left is (1,1) botom right is (n,n)
# map is connected top of (1,1) is (N,1), left of (1,1) is (1,N)

# vivargie causes rain cloud in (N,1), (N,2), (N-1, 1), (N-1,2)
# command M times
# i th commmand has d_i(direction) and s_i(distance)
# there are a total of 8 directions (each as integer)
# 1: l
# 2: ul
# 3: u
# 4: ur
# 5: r
# 6: br
# 7: b
# 8: bl

# Analyzing the command
# 1. all clouds move to d_i by s_i
# 2. in the positions of the clouds, rain falls (+1water in block)
# 3. all clouds disappear
# 4. (water copy command for blocks that had +1 water)
#       diagonal increase for neighboring blocks (ul, ur, bl, br)
#   Conditions
#   a) those who are out of bound are not considered
# 5. For all blocks that have an amount of water more than 2, cloud appears
#   for the block that has a cloud decreases in water amount by 2
#   Conditions
#   a) the blocks that has clouds should not be one of the blocks where cloud disappeared

# Solve: Find the total amount of water after M times

N, M = map(int, input().split())
A = []
# for each element in command 0 index is direction 1 index is amount
commands = []

clouds = {}

for i in range(N):
    temp = []
    for k in input().split():
        temp.append(int(k))
    A.append(temp)
for i in range(M):
    d_i, s_i = map(int, input().split())
    commands.append([d_i, s_i])


def parse_dir(integer):
    delta = [0, 0]
    # left
    if integer == 1:
        delta[1] = -1
    # up left
    elif integer == 2:
        delta[0] = -1
        delta[1] = -1
    # up
    elif integer == 3:
        delta[0] = -1
    # up right
    elif integer == 4:
        delta[0] = -1
        delta[1] = 1
    # right
    elif integer == 5:
        delta[1] = 1
    # bottom right
    elif integer == 6:
        delta[0] = 1
        delta[1] = 1
    # bottom
    elif integer == 7:
        delta[0] = 1
    # bottom left
    elif integer == 8:
        delta[0] = 1
        delta[1] = -1
    else:
        raise Exception("direction is not valid")
    return delta


def parse_command(element):
    delta = parse_dir(element[0])
    repeat = element[1]
    return delta, repeat


def gen_pos_id(r, c):
    return f'{r}_{c}'


def parse_pos_id(id):
    splitted = id.split("_")
    if len(splitted) != 2:
        raise Exception("Invalide position id")
    return int(splitted[0]), int(splitted[1])


def rain_water(r, c):
    global A
    A[r-1][c-1] += 1


def check_bound(r, c):
    global N
    if r < 1 or r > N:
        return False
    if c < 1 or c > N:
        return False
    return True


def copy_water(new_clouds):
    global A
    for key in new_clouds.keys():
        r, c = parse_pos_id(key)
        ul = [r-1, c-1]
        ur = [r-1, c+1]
        bl = [r+1, c-1]
        br = [r+1, c+1]
        ul_ok = check_bound(ul[0], ul[1])
        ur_ok = check_bound(ur[0], ur[1])
        bl_ok = check_bound(bl[0], bl[1])
        br_ok = check_bound(br[0], br[1])
        if ul_ok:
            if (A[ul[0] - 1][ul[1] - 1] > 0):
                A[r-1][c-1] += 1
        if ur_ok:
            if (A[ur[0] - 1][ur[1] - 1] > 0):
                A[r-1][c-1] += 1
        if bl_ok:
            if (A[bl[0] - 1][bl[1] - 1] > 0):
                A[r-1][c-1] += 1
        if br_ok:
            if (A[br[0] - 1][br[1] - 1] > 0):
                A[r-1][c-1] += 1


def make_clouds(previous_clouds):
    global A
    global N
    created_clouds = {}
    for i in range(N):
        for j in range(N):
            water = A[i][j]
            if water >= 2:
                cloud_id = gen_pos_id(i + 1, j + 1)
                # step 5 condition a) 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다
                if not previous_clouds.get(cloud_id):
                    created_clouds[cloud_id] = True
                    A[i][j] -= 2
    return created_clouds


# initial clouds
N_1 = gen_pos_id(N, 1)
N_2 = gen_pos_id(N, 2)
Nsub1_1 = gen_pos_id(N-1, 1)
Nsub1_2 = gen_pos_id(N-1, 2)
clouds[N_1] = True
clouds[N_2] = True
clouds[Nsub1_1] = True
clouds[Nsub1_2] = True

for i in range(M):
    delta, repeat = parse_command(commands[i])
    new_clouds = {}
    for key in clouds.keys():
        r, c = parse_pos_id(key)
        new_r = r
        new_c = c
        # step 1 (this takes time)
        consider_repeat = repeat % N
        # for k in range(consider_repeat):
        new_r = new_r + delta[0] * consider_repeat
        new_c = new_c + delta[1] * consider_repeat
        if new_r == 0:
            new_r = N
        elif new_r == N + 1:
            new_r = 1
        elif new_r < 0:
            new_r = new_r + N
        elif new_r > N + 1:
            new_r = new_r - N

        if new_c == 0:
            new_c = N
        elif new_c == N + 1:
            new_c = 1
        elif new_c < 0:
            new_c = new_c + N
        elif new_c > N + 1:
            new_c = new_c - N
        new_cloud_id = gen_pos_id(new_r, new_c)
        new_clouds[new_cloud_id] = True
        # step 2
        rain_water(new_r, new_c)
    # step 3 (Delete all couds)
    clouds = {}
    # step 4 (Copy water for blocks with added water)
    copy_water(new_clouds)
    # step 5 (Make clouds)
    clouds = make_clouds(new_clouds)
    # print(clouds)

total_water = 0
for i in range(N):
    for j in range(N):
        total_water += A[i][j]

print(total_water)
