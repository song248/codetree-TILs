n, k = tuple(map(int, input().split()))
u = [(0, False) for _ in range(n)]
d = [(0, False) for _ in range(n)]


def shift():
    temp = u[n - 1]
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

def can_go(idx):
    if idx == n:
        return True
    stability, occupied = u[idx]
    return stability > 0 and not occupied

def move(idx):
    curr_stability, _ = u[idx]
    u[idx] = (curr_stability, False)
    if idx + 1 < n:
        next_stability, _ = u[idx + 1]
        u[idx + 1] = (next_stability - 1, True)

def move_all():
    for i in range(n - 1, -1, -1):
        _, occupied = u[i]
        if occupied and can_go(i + 1):
            move(i)

def add():
    stability, occupied = u[0]
    if stability > 0 and not occupied:
        u[0] = (stability - 1, True)

def simulate():
    shift()
    move_all()
    add()
    _, occupied = u[n - 1]
    if occupied:
        move(n - 1)

def done():
    unstable_cnt = 0
    for stability, _ in u:
        if not stability:
            unstable_cnt += 1

    for stability, _ in d:
        if not stability:
            unstable_cnt += 1
    
    return unstable_cnt >= k

given_row = list(map(int, input().split()))
for i, stability in enumerate(given_row[:n]):
    u[i] = (stability, False)
for i, stability in enumerate(given_row[n:]):
    d[i] = (stability, False)

trial = 0
while not done():
    simulate()
    trial += 1

print(trial)