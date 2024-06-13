from collections import deque

# 숲의 모양을 어떻게 짤 것인가
# R, C 크기대로 잡으면 골렘이 초과되면 에러가 발생할텐데
MAX_L = 70
forest = [[0] * MAX_L for _ in range(MAX_L + 3)]
# 숲과 똑같은 모양의 출구 저장 공간(요정 이동시 활용)
golem_exit = [[False] * MAX_L for _ in range(MAX_L + 3)]
answer = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def inRange(y, x):
    return 3 <= y < R + 3 and 0 <= x < C

def clean_forest():
    for i in range(R+3):
        for j in range(C):
            forest[i][j] = 0
            golem_exit[i][j] = False

# (y, x)와 (y-1, x)가 forest안에 있는지 -> 이동전 중심과 이동후 중심
# 중심에 대해 상하좌우 네 방향에 대해서도 확인
# y는 forest 안에 한칸이라도 걸쳐야하니 R+3보다 작아야 범위안에 존재
# y 최소범위를 확인하지 않는 이유는 초기위치 0으로 입력을 주기 때문에
def can_move(y, x):
    chk = (x-1 >= 0 and x+1 < C and y+1 < R+3)
    chk = chk and forest[y][x]==0
    chk = chk and forest[y+1][x]==0
    chk = chk and forest[y][x-1]==0
    chk = chk and forest[y][x+1]==0
    chk = chk and forest[y-1][x]==0
    chk = chk and forest[y-1][x-1]==0
    chk = chk and forest[y-1][x+1]==0
    return chk

def fairy_dfs(y, x):
    result = y
    dq = deque([(y, x)])
    visited = [[False] * C for _ in range(R+3)]
    visited[y][x] = True
    while dq:
        c_y, c_x = dq.popleft()
        for i in range(4):
            ny = c_y+dy[0]
            nx = c_x+dx[0]
            # 골렘 내부 혹은 출구가 이어진 다른 골렘
            if inRange(ny, nx) and not visited[ny][nx] and \
            (forest[ny][nx] == forest[c_y][c_x] or (forest[ny][nx] != 0 and golem_exit[c_y][c_x])):
                dq.append((ny, nx))
                visited[ny][nx] = True
                result = max(result, ny)
    return result

# golem move down
# y: 시작행 / X: 시작열 / d: 출구방향 / id: 몇번째 골렘
# 출구위치 d의 경우
# 서쪽 이동시 (d+3)%4
# 동쪽 이동시 (d+1)%4
def golem_down(y, x, d, id):
    global R, C, K
    # down
    if can_move(y+1, x):
        golem_down(y+1, x, d, id)
    # west & down
    elif can_move(y+1, x-1):
        golem_down(y+1, x-1, (d+3)%4, id)
    # east & down
    elif can_move(y+1, x+1):
        golem_down(y+1, x+1, (d+1)%4, id)
    # can't move
    else:
        # golem out of forest
        if not inRange(y-1, x-1) or not inRange(y+1, x+1):
            clean_forest()
        # fairy 열 계산
        else:
            # 골렘 중심 및 십자 위치 및 출구 위치
            forest[y][x] = id
            for i in range(4):
                forest[y+dy[i]][x+dx[i]] = id
            golem_exit[y+dy[d]][x+dx[d]] = True
            global answer
            # R에 +3을 
            answer += fairy_dfs(y, x)-3+1

R, C, K = map(int, input().split())
for id in range(1, K+1): 
    x, d = map(int, input().split())
    golem_down(0, x-1, d, id)
print(answer)