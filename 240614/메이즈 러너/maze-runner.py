N,M,K = map(int, input().split())
maze = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    maze[i] = [0] + list(map(int, input().split()))
parti = [tuple(map(int, input().split())) for _ in range(M)]
parti = [(-1, -1)] + parti
exit = tuple(map(int, input().split()))
ans = 0
sx, sy, sq_size = 0, 0, 0

tmp_maze = [[0] * (N+1) for _ in range(N+1)]

# 참가자 이동
# 출구까지 거리가 가까워지면 
def move():
    global exit, ans
    for i in range(1, M+1):
        if parti[i] == exit:
            continue
        tx, ty = parti[i][0], parti[i][1]
        if tx != exit[0]:
            nx, ny = tx, ty
            if nx < exit[0]:
                nx += 1
            else:
                nx -= 1
            if maze[nx][ny] == 0:
                parti[i] = (nx, ny)
                ans += 1
                continue
        # 상하 움직임 먼저 고려
        if ty != exit[1]:
            nx, ny = tx, ty
            if ny < exit[1]:
                ny += 1
            else:
                ny -= 1
            if maze[nx][ny] == 0:
                parti[i] = (nx, ny)
                ans += 1
                # 한번에 한칸만 이동
                continue
        

# 정사각형 잡기
# 최소 참가자 1명, 탈출구 포함
# 참가자와 출구가 포함될려면 크기 2부터(2~N+1까지 탐색)
def make_sq():
    global sx, sy, sq_size
    for size in range(2, N+1):
        # 정해진 사이즈만큼 이동 가능한 범위의 r,c
        for x1 in range(1, N-size+2):
            for y1 in range(1, N-size+2):
                x2 = x1+size-1
                y2 = y1+size-1
                # 출구가 있는지
                # if x1 > exit[0] or x2 < exit[0] or y1 > exit[1] or y2 > exit[1]:
                if not (x1 <= exit[0] <= x2 and y1 <= exit[1] <= y2):
                    continue
                in_sq = False
                for k in range(1, M+1):
                    tx, ty = parti[k]
                    if x1 <= tx <= x2 and y1 <= ty <= y2:
                        if not (tx == exit[0] and ty == exit[1]):
                            in_sq = True
                if in_sq:
                    sx = x1
                    sy = y1
                    sq_size = size
                    return

def rotate():
    global exit
    # 범위 내 벽돌 데미지
    for i in range(sx, sx+sq_size):
        for j in range(sy, sy+sq_size):
            if maze[i][j] != 0:
                maze[i][j] -= 1
    # 회전 영역 추출 및 회전
    for x in range(sx, sx + sq_size):
        for y in range(sy, sy + sq_size):
            ox, oy = x-sx, y-sy
            rx, ry = oy, sq_size-ox-1
            tmp_maze[rx+sx][ry+sy] = maze[x][y]
    for x in range(sx, sx + sq_size):
        for y in range(sy, sy + sq_size):
            maze[x][y] = tmp_maze[x][y]

    # 참가자 회전
    for k in range(1, M+1):
        tx, ty = parti[k]
        if sx <= tx < sx+sq_size and sy <= ty < sy+sq_size:
            # 회전하려는 위치의 점을 (0,0)으로 옮김
            # 이후 90도 회전 후 값 복원
            # (x, y) -> (y, x+size-1)
            ox, oy = tx-sx, ty-sy
            rx, ry = oy, sq_size-ox-1
            parti[k] = (rx+sx, ry+sy)
            
    # 출구 회전
    ex, ey = exit[0], exit[1]
    ox, oy = ex-sx, ey-sy
    rx, ry = oy, sq_size-ox-1
    exit = (rx+sx, ry+sy)

for _ in range(K):
    move()
    all_escape = True
    for i in range(1, M+1):
        if parti[i] != exit:
            all_escape = False
    if all_escape:
        break
    make_sq()
    rotate()
    
print(ans)
print(exit[0], exit[1])