from collections import deque

n, k = map(int, input().split())
safe = list(map(int, input().split()))

belt = deque([])
for i in safe:
    belt.append([i, 0])

cnt = 0
while True:
    k_list = list(map(lambda x: x[0], belt))      
    if k_list.count(0) == k:
        break
    tmp = belt.pop()
    belt.appendleft(tmp)
    for i in range(n-1):
        if belt[i][1] == 1:
            if belt[i+1][0] != 0 and belt[i+1][1] == 0:
                belt[i][1] = 0
                belt[i+1][1] = 1 
                belt[i+1][0] -= 1
    if belt[n-1][1] >= 1:
        belt[n-1][1] = 0
    if belt[0][1] == 0:
        belt[0][1] += 1
        belt[0][0] -= 1
    cnt += 1

    if cnt > 10:
        break
print(cnt)