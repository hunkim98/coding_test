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

def bfs_dis(start_r, start_c, destinations):
    # destinations is a dict with pos as keys
    global grids
    visited = {} # this is a dict of pos_id
    queue = []
    queue.append([start_r, start_c, 0]) # start position
    # we also input the level
    # we have to check for u, l, b, r
    u_delta = [-1, 0]
    l_delta = [0, -1]
    b_delta = [1, 0]
    r_delta = [0, 1]

    least_distance = 500

    nearest_des = []

    has_at_least_one_el = False
    while len(queue) != 0:
        explore = queue.pop(0)
        explore_pos_id = gen_pos_id(explore[0], explore[1])
        # if visited.get(explore_pos_id):
        #     continue

        distance = explore[2]
        if least_distance < distance:
            break
        if destinations.get(explore_pos_id):
            if not has_at_least_one_el:
                nearest_des.append(explore_pos_id)
            else:
                first_el = nearest_des[0]
                first_r, first_c = parse_pos_id(first_el)
                if explore[0] < first_r:
                    nearest_des.insert(0, explore_pos_id)
                elif explore[0] == first_r:
                    if explore[1] < first_c:
                        nearest_des.insert(0, explore_pos_id)
                    else:
                        nearest_des.append(explore_pos_id)
                else:
                    nearest_des.append(explore_pos_id)
                has_at_least_one_el = True
            if least_distance > distance:
                least_distance = distance
        # print(explore_pos_id, distance, least_distance)
        visited[explore_pos_id] = True

        u_r = explore[0] + u_delta[0]
        u_c = explore[1] + u_delta[1]
        u_id = gen_pos_id(u_r, u_c)
        u_visited = visited.get(u_id)
        if get_wall(u_r, u_c) == 0 and u_visited is None:
            if least_distance > distance + 1:
                visited[u_id] = False
                queue.append([u_r, u_c, distance + 1])

        l_r = explore[0] + l_delta[0]
        l_c = explore[1] + l_delta[1]
        l_id = gen_pos_id(l_r, l_c)
        l_visited = visited.get(l_id)
        if get_wall(l_r, l_c) == 0 and l_visited is None:
            if least_distance > distance + 1:
                visited[l_id] = False
                queue.append([l_r, l_c, distance + 1])

        b_r = explore[0] + b_delta[0]
        b_c = explore[1] + b_delta[1]
        b_id = gen_pos_id(b_r, b_c)
        b_visited = visited.get(b_id)
        if get_wall(b_r, b_c) == 0 and b_visited is None:
            if least_distance > distance + 1:
                visited[b_id] = False
                queue.append([b_r, b_c, distance + 1])

        r_r = explore[0] + r_delta[0]
        r_c = explore[1] + r_delta[1]
        r_id = gen_pos_id(r_r, r_c)
        r_visited = visited.get(r_id)
        if get_wall(r_r, r_c) == 0 and r_visited is None:
            if least_distance > distance + 1:
                visited[r_id] = False
                queue.append([r_r, r_c, distance + 1])

    return least_distance, nearest_des







def find_passenger():
    global grids
    global passengers
    global taxi_r
    global taxi_c

    dis, des_list = bfs_dis(taxi_r, taxi_c, passengers) # passengers is a dict
    pass_r = -1
    pass_c = -1
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












