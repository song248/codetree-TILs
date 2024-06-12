import heapq

def dijkstra():
    global short_cut
    short_cut = [INF] * N
    visit = [False] * N
    short_cut[S] = 0
    
    for i in range(N):
        v = -1
        min_dis = INF
        for j in range(N):
            if not visit[j] and min_dis > short_cut[j]:
                v = j
                min_dis = short_cut[j]
        if v == -1:
            break
        visit[v] = True
        for j in range(N):
            if land[v][j] != INF and short_cut[j] > short_cut[v] + land[v][j]:
                short_cut[j] = short_cut[v] + land[v][j]

# status == 100
def make_land(n, m, arr):
    global N, M, land
    N, M = n, m
    land = [[INF]*N for _ in range(N)]
    for i in range(N):
        land[i][i] = 0  # 도시 자신에게 가는 비용은 0
    for i in range(0, M*3, 3):
        u, v, w = arr[i], arr[i+1], arr[i+2]
        land[u][v] = min(land[u][v], w)
        land[v][u] = min(land[v][u], w)

# status == 200
def create_trip(id, rev, des):
    trip_in[id] = True
    dis = rev-short_cut[des]
    # 기존 id rev des dis
    heapq.heappush(hq, (-dis, id, rev, des))

# status == 300
def delete_trip(id):
    if trip_in[id] == True:
        trip_out[id] = True

# status == 400
def sell_trip():
    while hq:
        p = hq[0]
        if p[0]*(-1) < 0 or p[0]*(-1) == INF:
            break
        heapq.heappop(hq)
        if not trip_out[p[1]]:
            return p[1]
    return -1

# status == 500
def change_S(ss):
    global S
    S = ss
    dijkstra()
    tmp_pck = []
    # 출발지가 바뀌었으니 기존 여행 상품 업데이트
    while hq:
        tmp_pck.append(heapq.heappop(hq))
    for p in tmp_pck:
        create_trip(p[1], p[2], p[3])

INF = float('inf')
land = []    # 관광지 간 가중치 행렬
short_cut = []    # 도시 간 최단경로
trip_in = []    # 여행상품이 만들어진적 있는지
trip_out = []    # 여행상품 취소 여부
S = 0    # 초기 출발지
hq = []
MAX_ID = 30000
trip_in = [False] * MAX_ID # 여행상품 생성 전적 상태 배열 초기화
trip_out = [False] * MAX_ID  # 여행상품 취소 상태 배열 초기화
# global trip_in, trip_out

Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    T = query[0]
    
    # 쿼리의 종류에 따라 필요한 함수들을 호출하여 처리합니다
    if T == 100:
        make_land(query[1], query[2], query[3:])
        dijkstra()
    elif T == 200:
        id, revenue, dest = query[1], query[2], query[3]
        create_trip(id, revenue, dest)
    elif T == 300:
        id = query[1]
        delete_trip(id)
    elif T == 400:
        print(sell_trip())
    elif T == 500:
        change_S(query[1])