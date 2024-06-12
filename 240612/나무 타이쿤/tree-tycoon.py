n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
# 이동방향
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, 1, 1, 0, -1, -1, -1, 0, 1]
# 영양제 초기 위치
nutrition = [[n-2, 0], [n-2, 1], [n-1, 0], [n-1, 1]]
# 보드 범위 밖인 경우
def board_chk(movement):
    if movement >= n:
        return movement%n
    if movement < 0:
        return movement+n
    return movement
for _ in range(m):
    d, p = map(int, input().split())
    # d, p 에 따른 이동(방향, 칸수)
    for nutri in nutrition:
        nutri[0] = board_chk(nutri[0] + dx[d]*p)
        nutri[1] = board_chk(nutri[1] + dy[d]*p)
    # 영양제 투여
    for nut in nutrition:
        board[nut[0]][nut[1]] += 1
    # 대각체크 및 성장
    cnt = 0
    grow_list = []
    for nut in nutrition:
        cnt = 0
        for d in [2, 4, 6, 8]:
            nx = nut[0] + dx[d]
            ny = nut[1] + dy[d]
            if nx >= 0 and nx < n and ny >= 0 and ny <n:
                if board[nx][ny] >= 1:
                    cnt += 1
        grow_list.append([nut, cnt])
    for gr in grow_list:
        board[gr[0][0]][gr[0][1]] +=  gr[1]
    # 길이 2 이상 잘라내고 영양제 투여
    # 기존 nutrition에 없어야 함
    new_nutrition = []
    for i in range(n):
        for j in range(n):
            if [i, j] not in nutrition:
                if board[i][j] >= 2:
                    board[i][j] -= 2
                    new_nutrition.append([i, j])
    nutrition = new_nutrition
ans = 0
for bo in board:
    ans += sum(bo)
print(ans)