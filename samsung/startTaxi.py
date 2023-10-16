# 1) 손님을 도착지로 데려다줄때마다 연료가 충전
# 2) 연료가 0이면 그 날 업무는 끝

# 목표 승객: M
# Area of movement N x N
# each block in N x N is either 1) empty, 2) wall
# if taxi is in empty block, can go up left bottom right
# Taxi movement Condition
# use shortest path (BFS)

# M customers are in one block in N x N
# Multiple customers cannot ride together
# one customer per drive (max to M drive times)
# customers do not move
# cannot leave or enter other than their start place and destination

# Customer choosing algorithm
# 1. 최단거리가 가장 짧은 승객
# 2. (여려명이 최단거리가 동일할 경우) 열 (column), 행(row) 번호가 가장 작은 승객
# 최단거리란? 택시와 승객 사이의 거리 (BFS)

# Movement Conditions
# 1. one move = one fuel
# 2. if success destination, fuel recharge by x2 of consumed fuel
# 3. if fuel is 0 while moving, then job is finished
# (when fuel is 0 while driving, it is counted as failure)

# solution
# check if all customers can be deliverd, and if so, print the leftover fuel

N, M, F = map(int, input().split()) # N is map size, M is passengers
# F is total fuel (F is infinite!)

grids = []

passengers = {}

for i in range(N):
    values = input().split() # values is string
    temp_row = []
    for j in values:
        info = int(j)
        temp_row.append(info)  # 1 is wall 0 is empty
    grids.append(temp_row)

taxi_r, taxi_c = map(int, input().split())

def gen_pos_id(r, c):
    return f"{r}_{c}"

def parse_pos_id(x_y):
    splitted = x_y.split("_")
    r = int(splitted[0])
    c = int(splitted[1])
    return r, c


for i in range(M):
    pas_r, pas_c, des_r, des_c = map(int, input().split())
    pos_id = gen_pos_id(pas_r, pas_c)
    des_id = gen_pos_id(des_r, des_c)
    passengers[pos_id] = des_id # passengers destination info

# if fuel is 0 while driving print -1

def get_wall(r, c):
    # returns either 0(empty), 1(wall), -1(invalid)
    global N
    global grids
    if r < 1 or r > N:
        return -1
    if c < 1 or c > N:
        return -1
    real_r = r - 1
    real_c = c - 1
    return grids[real_r][real_c]

# u l b r
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs_dis(start_r, start_c, destinations):
    # destinations is a dict with pos as keys
    global N
    global grids
    global dx
    global dy
    queue = []
    visited = [[False] * N for _ in range(N)]
    queue.append([start_r, start_c, 0]) # start position
    visited[start_r - 1][start_c - 1] = True

    least_distance = 5000
    nearest_des = []

    while len(queue) != 0:
        explore = queue.pop(0)
        r, c, dis = explore
        r_c = gen_pos_id(r,c)

        if least_distance < dis:
            break

        if destinations.get(r_c) is not None:
            if len(nearest_des) == 0:
                nearest_des.append(r_c)
            else:
                first_el = nearest_des[0]
                first_r, first_c = parse_pos_id(first_el)
                if r < first_r:
                    nearest_des.insert(0, r_c)
                elif r == first_r:
                    if c < first_c:
                        nearest_des.insert(0, r_c)
                    else:
                        nearest_des.append(r_c)
                else:
                    nearest_des.append(r_c)
            least_distance = dis


        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            n_id = gen_pos_id(nr, nc)
            if get_wall(nr, nc) != 0:
                continue
            if visited[nr - 1][nc - 1]:
                continue
            visited[nr - 1][nc - 1] = True
            queue.append([nr, nc, dis + 1])


    return least_distance, nearest_des


def find_passenger():
    global grids
    global passengers
    global taxi_r
    global taxi_c

    dis, des_list = bfs_dis(taxi_r, taxi_c, passengers) # passengers is a dict
    pass_r = -1
    pass_c = -1
    # print(des_list)
    des_list_len = len(des_list)
    if des_list_len == 0:
        return -1, -1, -1
    else:
        pass_r, pass_c = parse_pos_id(des_list[0])

    if pass_r == -1 or pass_c == -1:
        raise Exception("wrong passenger info!")

    return pass_r, pass_c, dis


carried_pass = 0

while F >= 0:
    next_r, next_c, fuel_count = find_passenger()
    if next_r == -1 and next_c == -1 and fuel_count == -1:
        # no passengers
        break
    if F - fuel_count < 0:
        break
    else:
        F = F - fuel_count

    taxi_r, taxi_c = next_r, next_c
    pass_id = gen_pos_id(next_r, next_c)
    pass_des = passengers.get(pass_id)
    if pass_des is None:
        raise Exception("passenger destination undefined")
    temp_pass_des = {}
    temp_pass_des[pass_des] = True
    des_fuel_count, arrive_des = bfs_dis(taxi_r, taxi_c, temp_pass_des)
    if len(arrive_des) != 1:
        break
    passengers.pop(pass_id) # pop the passenger

    if F - des_fuel_count < 0:
        break
    else:
        F = F - des_fuel_count + des_fuel_count * 2
    carried_pass = carried_pass + 1
    taxi_r, taxi_c = parse_pos_id(pass_des)

    if carried_pass == M:
        break


if carried_pass == M:
    print(F)
else:
    print(-1)





# 6 3 100
# 0 0 1 0 0 0
# 0 0 1 0 0 0
# 0 0 0 1 0 0
# 0 0 0 1 0 0
# 0 0 0 0 0 0
# 0 0 0 1 0 0
# 6 5
# 2 2 5 6
# 5 4 1 6
# 4 2 3 5












