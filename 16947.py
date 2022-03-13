from collections import defaultdict, deque
import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def dfs(u, p):
    global cycle_num, visit_cnt, parent, mark

    #완전 방문한경우 리턴
    if visit_cnt[u] == 2:
        return

    #부분적 방문인 경우
    if visit_cnt[u] == 1:
        cycle_num += 1
        cur = p
        mark[cur] = cycle_num

        #사이클 추적
        while cur != u:
            cur = parent[cur]
            mark[cur] = cycle_num

        return

    parent[u] = p
    
    #부분적으로 방문완료
    visit_cnt[u] = 1

    #dfs
    for v in graph[u]:
        if v == parent[u]:
            continue
        dfs(v, u)

    #완전히 방문완료
    visit_cnt[u] = 2
    
def bfs():
    while q:
        element, distance = q.popleft()

        distances[element] = distance
        for v in graph[element]:
            if v not in visited:
                visited.add(v)
                q.append((v, distance+1))

#노드의 갯수
n = int(input())

graph = defaultdict(list) #그래프

#사이클 추출을 위한 변수
visit_cnt = [0] * (n+1)
parent = [0] * (n+1)
mark = [0] * (n+1)
cycle_num = 0

#사이클 추출 후 시작점 판별을 위한 차수와
#순환선까지의 거리를 저장하기위한 배열
degree = [0] * (n+1)
distances = [0] * (n+1)

#사이클 추출 후 BFS를 수행하기 위한 큐와 visited set
q = deque()
visited = set()

#그래프 입력
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    degree[a] += 1
    degree[b] += 1

#깊이우선탐색
dfs(1,0)

#사이클 그래프 추출
cycles = set()
for i in range(n+1):
    if mark[i] != 0:
        cycles.add(i)

for e in cycles:
    #사이클 구성하는경우 이미 방문한것으로 취급
    visited.add(e)
    
    #사이클 구성요소 중에 차수가 3이상 - 순환선에서 갈림길이 있다는 것이므로
    #BFS 시작점으로 큐에 삽입
    if degree[e] > 2:
        q.append((e,0))

#BFS 시작점을 넣은 채로 너비우선탐색 하면서 거리 재기
bfs()

#순환선까지의 거리 출력
print(*distances[1:])