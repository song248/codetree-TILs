n = int(input())
work = []
for _ in range(n):
    work.append(list(map(int, input().split())))
dp = [0]*(n+1)

for i in range(n):
    for j in range(work[i][0]+i, n+1):
        if dp[j] < dp[i]+work[i][1]:
            dp[j] = dp[i]+work[i][1]
print(dp[-1])