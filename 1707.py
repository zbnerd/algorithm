import sys
from collections import defaultdict, deque

input = sys.stdin.readline

#너비우선탐색
def bfs(start):
    q = deque()
    
    visited[start] = 1
    q.append(start)
    while q:
        pop = q.popleft()
        #그래프를 순회하면서 인접 정점과 다른색깔을 칠하게 하는 변수

        for adj in graph[pop]:
            if visited[adj] == 0:
                visited[adj] = -visited[pop]
                q.append(adj)
            
            else :
                if visited[adj] == visited[pop]:
                    return False

    return True

for _ in range(int(input())):
    #정점, 간선의 갯수
    v, e = map(int,input().split())
    flag = True

    #그래프 입력받기
    graph = defaultdict(list)
    visited = [0] * (v+1)
    for _ in range(e):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    #1번부터 모든정점 너비우선탐색
    for k in range(1,v+1):
        if visited[k] == 0:
            if not bfs(k):
                flag = False
                break
    
    print('YES' if flag else 'NO')