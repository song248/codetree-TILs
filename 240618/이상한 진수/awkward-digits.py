a = str(input())
b = str(input())

a_list = set()
b_list = set()

for i in range(len(a)):
    for bit in [0, 1]:
        new_a = a[:i] + str(bit) + a[i+1:]
        a_list.add(int(new_a, 2))

for i in range(len(b)):
    for bit in [0, 1, 2]:
        new_b = b[:i] + str(bit) + b[i+1:]
        b_list.add(int(new_b, 3))
print(list(a_list.intersection(b_list))[0])