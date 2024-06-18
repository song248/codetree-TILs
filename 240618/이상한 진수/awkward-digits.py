binary = list(map(int, input()))
length = len(binary)

INT_MIN = -9999999
ans = INT_MIN
for i in range(length):
    binary[i] = 1-binary[i]

    num = 0
    for j in range(length):
        num += (2**(length-j-1)) * binary[j]
    ans = max(ans, num)
    binary[i] = 1-binary[i]
print(ans)