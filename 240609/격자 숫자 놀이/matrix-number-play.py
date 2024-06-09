r,c,k = map(int, input().split())
A = []
for i in range(3):
    A.append(list(map(int, input().split())))

def list_cnt(c_list):
    tmp_dict = dict()
    for c in c_list:
        if c != 0:
            if c in tmp_dict:
                cnt = tmp_dict[c]
                tmp_dict[c] = cnt + 1
            else:
                tmp_dict[c] = 1
    return tmp_dict

def fill_zero(A, max_len):
    for a in A:
        while len(a) < max_len:
            a.append(0)
    return A

def cal_row(A):
    new_A = []
    for a in A:
        t_dict = list_cnt(a)
        t_list_1 = []
        for i in t_dict:
            t_list_1.append([i, t_dict[i]])
        t_list_1.sort(key = lambda x: (x[1], x[0]))
        t_list_2 = []
        for tt in t_list_1:
            t_list_2.append(tt[0])
            t_list_2.append(tt[1])
        if len(t_list_2) > 100:
            t_list_2 = t_list_2[:100]
        new_A.append(t_list_2)
    return fill_zero(new_A, max(map(len, new_A)))

def cal_col(A):
    new_A = []
    # *A는 리스트 A의 각 요소(행)를 개별적으로 풀어냄
    # zip은 이렇게 풀려진 요소들을 튜플로 모아 반복자(iterator)를 생성
    # zip(*A)는 원본 리스트 A의 열(column)들을 튜플로 묶어 반환
    # map(list, zip(*A))는 각 튜플을 리스트로 변환
    for a in map(list, zip(*A)):
        t_dict = list_cnt(a)
        t_list_1 = []
        for i in t_dict:
            t_list_1.append([i, t_dict[i]])
        t_list_1.sort(key = lambda x: (x[1], x[0]))
        t_list_2 = []
        for tt in t_list_1:
            t_list_2.append(tt[0])
            t_list_2.append(tt[1])
        if len(t_list_2) > 100:
            t_list_2 = t_list_2[:100]
        new_A.append(t_list_2)
    new_A = fill_zero(new_A, max(map(len, new_A)))
    return list(map(list, zip(*new_A)))

sec = 0
while True:
    # 조건 확인 K
    if r <= len(A[0]) and c <= len(A):
        if A[r-1][c-1] == k:
            print(sec)
            break
    # 조건 확인 sec
    if sec > 100:
        print(-1)
        break
    # 행 열 길이 비교
    if len(A[0]) <= len(A):
        # 행 연산
        A = cal_row(A)
    else:
        # 열 연산
        A = cal_col(A)
    sec += 1