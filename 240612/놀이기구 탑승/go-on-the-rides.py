n = int(input())
std_list = [0 for _ in range(n * n + 1)]
friends = [[False for _ in range(n * n + 1)] for _ in range(n * n + 1)]
play = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] 

# 주변 상황 탐색
# need: 주변 빈칸 수, 좋아하는 친구가 있는지
def nearby(num, x, y):
    empty_cell, like_friend = 0, 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= n:
            if play[nx][ny] == 0:
                empty_cell += 1
            elif friends[num][play[nx][ny]] == 1:
                like_friend += 1
    return (like_friend, empty_cell, -x, -y)

# 놀이기구 탑승(우선순위가 높은 위치 찾기)
# 1. like_friend가 많은 곳
# 2. empty_cell이 많은 곳
# 3. 행 작은 곳 -> 열 작은 곳
def on_the_play(std_num):
    # 행과 열이 -인 이유는 튜플 연산을 하기 위해
    best_place = (0, 0, -(n+1), -(n+1))
    for i in range(1, n+1):
        for j in range(1, n+1):
            if play[i][j] == 0:
                now_state = nearby(std_num, i, j)
                if best_place < now_state:
                    best_place = now_state
    play[-best_place[2]][-best_place[3]] = std_num

def get_score(x, y):
    f_cnt = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 1 <= nx <= n and 1 <= ny <= n and friends[play[x][y]][play[nx][ny]] == 1:
            f_cnt += 1
    if f_cnt <= 0:
        return 0
    else:
        return int(10**(f_cnt-1))

for i in range(1, n * n + 1):
    student_data = list(map(int, input().split()))
    
    std_list[i] = student_data[0]
    for friend_num in student_data[1:]:
        # 현재 번호에 친구 번호를 표시해줍니다.
        friends[std_list[i]][friend_num] = True

for i in range(1, n * n + 1):
    on_the_play(std_list[i])

score_list = []
for i in range(1, n+1):
    for j in range(1, n+1):
        score_list.append(get_score(i, j))
print(sum(score_list))