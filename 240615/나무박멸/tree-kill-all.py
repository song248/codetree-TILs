n, m, k, c = map(int, input().split())
board = [[0]*(n+1)]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))
# 나무 성장 정보
grown = [[0]*(n+1) for _ in range(n+1)]
# 제초제 정보
t_killer = [[0]*(n+1) for _ in range(n+1)]

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
dxc = [-1, 1, 1, -1]
dyc = [-1, -1, 1, 1]

def tree_grown():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            t_cnt = 0
            if board[i][j] > 0:
                for o in range(4):
                    nx = i + dx[o]
                    ny = j + dy[o]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if board[nx][ny] > 0:
                            t_cnt += 1
            board[i][j] += t_cnt

def breeding():
    # 성장정보 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            grown[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] <= 0:  # 벽이 아닐때
                continue
            d_cnt = 0
            # 주변 빈칸 카운트
            for o in range(4):
                nx = i + dx[o]
                ny = j + dy[o]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if t_killer[nx][ny] == 0 and board[nx][ny] == 0:
                        d_cnt += 1
            # 번식
            for o in range(4):
                nx = i + dx[o]
                ny = j + dy[o]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if t_killer[nx][ny] == 0 and board[nx][ny] == 0:
                        grown[nx][ny] += board[i][j] // d_cnt
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            board[i][j] += grown[i][j]

def kill_the_tree():
    global ans
    # 모든 위치에 대해
    # nx, ny k만큼 제초제 뿌려서 박멸 나무 수 카운드
    # 그 값이 max인 위치 찾아내기
    max_kill = 0
    rx, ry = 1, 1
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] <= 0:
                continue
            k_cnt = board[i][j]
            for o in range(4):
                nx, ny = i, j
                for _ in range(k):
                    nx = nx+dxc[o]
                    ny = ny+dyc[o]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if board[nx][ny] > 0:
                            k_cnt += board[nx][ny]
            if max_kill < k_cnt:
                max_kill = k_cnt
                rx, ry = i, j
    ans += max_kill
    # 제초제 살포
    if board[rx][ry] > 0:
        t_killer[rx][ry] = c
        board[rx][ry] = 0
        for o in range(4):
            nx, ny = rx, ry
            for _ in range(k):
                nx = nx + dxc[o]
                ny = ny + dyc[o]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if board[nx][ny] < 0:
                        break
                    if board[nx][ny] == 0:
                        t_killer[nx][ny] = c
                        break
                    t_killer[nx][ny] = c
                    board[nx][ny] = 0

def year():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if t_killer[i][j] > 0:
                t_killer[i][j] -= 1

for _ in range(m):
    tree_grown()
    breeding()
    year()
    kill_the_tree()

print(ans)