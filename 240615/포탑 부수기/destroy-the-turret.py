from collections import deque

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 최근 공격 했는지
rec = [[0]*M for _ in range(N)]
# 방문여부
vis = [[False]*M for _ in range(N)]
# 공격과 무관했는지
peace = [[False]*M for _ in range(N)]

turn = 0    # 언제 공격했는지 기록용
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dxs = [0, 0, 0, -1, -1, -1, 1, 1, 1]
dys = [0, -1, 1, 0, -1, 1, 0, -1, 1]

# laser attack 최단경로 탐색시 기록
# 경로 돌아가면서 공격
back_x = [[0]*M for _ in range(N)]
back_y = [[0]*M for _ in range(N)]

def choose_attacker():
    global live_turret
    # 터렛리스트 정보: x, y, 최근공격, 공격력
    # 정렬순서 공격력 약한 순 -> 가장 최근 공격 -> 행+열 -> 행
    live_turret = sorted(live_turret, key=lambda x: (x[3], -x[2], -(x[0]+x[1]), -x[1]))
    weakness = live_turret[0]
    x, y = weakness[0], weakness[1]
    board[x][y] += (N+M)
    rec[x][y] = turn
    peace[x][y] = True
    live_turret[0] = (x, y, rec[x][y], board[x][y])

def laser_attack():
    weakness = live_turret[0]
    sx,sy = weakness[0], weakness[1]
    power = weakness[3]
    strongest = live_turret[-1]
    ex, ey = strongest[0], strongest[1]
    
    dq = deque()
    vis[sx][sy] = True
    dq.append((sx,  sy))
    can_attack = False

    while dq:
        x, y = dq.popleft()
        if x == ex and y == ey:
            can_attack = True
            break
        for o in range(4):
            # 테두리를 넘어갈 수 있음 
            # n*m보다 커지면 0 위치로
            nx = (x+dx[o]+N)%N
            ny = (y+dy[o]+M)%M
            if vis[nx][ny]:    # 방문한 포탑 pass
                continue
            if board[nx][ny] == 0:    # 벽 pass
                continue
            vis[nx][ny] = True
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            dq.append((nx, ny))
    if can_attack:
        board[ex][ey] -= power
        if board[ex][ey] < 0:
            board[ex][ey] = 0
        peace[ex][ey] = True

        cx = back_x[ex][ey]
        cy = back_y[ex][ey]
        
        while not(cx == sx and cy == sy):
            board[cx][cy] -= power//2
            if board[cx][cy] < 0:
                board[cx][cy] = 0
            peace[cx][cy] = True
            next_cx = back_x[cx][cy]
            next_cy = back_y[cx][cy]
            cx, cy = next_cx, next_cy
    return can_attack

def bomb_attack():
    weakness = live_turret[0]
    sx,sy = weakness[0], weakness[1]
    power = weakness[3]
    strongest = live_turret[-1]
    ex, ey = strongest[0], strongest[1]

    for o in range(8):
        nx = (ex+dxs[o]+N)%N
        ny = (ey+dxy[o]+M)%M

        if nx == sx and ny == sy:
            contonue
        if nx == ex and ny == ey:
            board[nx][ny] -= power
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            peace[nx][ny] = True
        else:
            board[nx][ny] -= power//2
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            peace[nx][ny] = True

def recovery():
    for i in range(N):
        for j in range(M):
            if peace[i][j]:
                continue
            if board[i][j] != 0:
                board[i][j] += 1

for _ in range(K):
    live_turret = []
    for i in range(N):
        for j in range(M):
            if board[i][j]:
                live_turret.append((i, j, rec[i][j], board[i][j]))
    if len(live_turret) <= 1:
        break
    turn += 1
    for i in range(N):
        for j in range(M):
            vis[i][j] = False
            peace[i][j] = False
    choose_attacker()
    succeed = laser_attack()
    if not succeed:
        bomb_attack()
    recovery()

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, board[i][j])
print(ans)