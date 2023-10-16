# import queue

N, M = map(int, input().split())

grids = []
# N is row count M is column count
for i in range(N):
    row_info = input()
    temp_row = []
    for j in range(M):
        if row_info[j] == "1":
            # movable
            temp_row.append(1)
        elif row_info[j] == "0":
            # not movable
            temp_row.append(0)
        else:
            raise Exception("invalid number")
    grids.append(temp_row)

# from 1, 1 to N, M
# can move u b r l
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
def bfs():
    global dx
    global dy
    queue = [] # remember to pop(0)
    visited = [[False] * M for _ in range(N)]
    distances = [[0] * M for _ in range(N)]
    # row, column, distance
    queue.append([1,1,1])
    visited[0][0] = True
    distances[0][0] = 1
    while len(queue) != 0:
        item = queue.pop(0)
        r, c, dis = item

        if r == N and c == M:
            break

        for i in range(4):
            # check visited
            # check distance
            nr = r + dx[i]
            nc = c + dy[i]
            if nr < 1 or nr > N:
                continue
            if nc < 1 or nc > M:
                continue
            visitable = grids[nr-1][nc-1]
            if visitable == 0:
                continue
            is_visited = visited[nr-1][nc-1]
            if is_visited:
                continue
            # queue를 해야 할 때는 visited, distances를 for loop안에다 넣어라!
            # 왜냐하면 for loop 돌면서 다른 친구들도 해당 친구를 넣을 수 있으니깐!
            visited[nr - 1][nc - 1] = True
            distances[nr - 1][nc - 1] = dis + 1
            queue.append([nr, nc, dis + 1])


    return distances

print(bfs()[N-1][M-1])





