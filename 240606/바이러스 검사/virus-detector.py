n = int(input())
n_list = list(map(int, input().split()))
t, p = map(int, input().split())

# print(n)
# print(n_list)
# print(t, p)

x_p = 0

for i in n_list:
    if i-t > 0:
        if (i-t)//p == 0:
            x_p+=(i-t)//p
        else:
            x_p+=(i-t)//p+1
print(n+x_p)