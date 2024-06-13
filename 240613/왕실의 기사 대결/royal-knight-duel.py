from collections import deque
MAX_L = 41
MAX_N = 31

board = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
r = [0 for _ in range(MAX_N)]   # 기사 처음 위치(r,c)
c = [0 for _ in range(MAX_N)]
h = [0 for _ in range(MAX_N)]   # 기사 쉴드 (h,w)
w = [0 for _ in range(MAX_N)]
k = [0 for _ in range(MAX_N)]   # 기사 체력
before_k = [0 for _ in range(MAX_N)]    # deepcopy
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]

visited = [False for _ in range(MAX_N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 미리 움직여보고 가능하면 움직이고
# 아니면 그대로 두기
def chk_move(idx, d):
    dq = deque()
    
    # 초기화 작업
    # 이전 이동 가능 여부 확인때 업데이트 됐으므로
    for i in range(1, N+1):
        dmg[i] = 0
        visited[i] = False
        nr[i] = r[i]
        nc[i] = c[i]

    visited[idx] = True
    dq.append(idx)

    while dq:
        x = dq.popleft()
        nr[x] += dx[d]
        nc[x] += dy[d]
        # board 밖으로 움직이면 불가
        if nr[x] < 1 or nc[x] < 1 or nr[x]+h[x]-1 > L or nc[x]+w[x]-1 > L:
            return False
        # 벽이면 불가능, 함정이면 데미지 계산
        for i in range(nr[x], nr[x]+h[x]):
            for j in range(nc[x], nc[x]+w[x]):
                if board[i][j] == 1:
                    dmg[x] += 1
                elif board[i][j] == 2:
                    return False
        # 다른 기사 영역과 겹칠시 해당 영역 이동시키기
        for i in range(1, N+1):
            if visited[i] or k[i] <= 0:
                continue
            if r[i] > nr[x]+h[x]-1 or nr[x] > r[i]+h[i]-1:
                continue
            if c[i] > nc[x]+w[x]-1 or nc[x] > c[i]+w[i]-1:
                continue
            # 여기까지 오면 안겹쳐서 이동에 포함시키는거
            visited[i] = True
            dq.append(i)
    dmg[idx] = 0
    return True

def knight_move(id, d):
    # 기사 체력이 0이면 아무것도 하지 않음
    if k[id] <= 0:
        return
    # 움직임이 가능한지 체그
    if chk_move(id, d):
        for i in range(1, N+1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]

L, N, Q = map(int, input().split())
for i in range(1, L+1):
    board[i][1:] = map(int, input().split())
for i in range(1, N+1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    before_k[i] = k[i]
for q in range(Q):
    idx, d = map(int, input().split())
    knight_move(idx, d)

answer = []
for i in range(1, N+1):
    if k[i] > 0:
        answer.append(before_k[i] - k[i])
print(sum(answer))