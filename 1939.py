import sys
from collections import defaultdict, deque

input = sys.stdin.readline

#1939 중량제한

#n - 섬의 수
#m - 다리의 수

n,m = map(int,input().split())

graph = defaultdict(dict)

bfs_q = deque()
visited = set()
visit_q = deque()

start = 1000000005
end = 0

#다리에 대한 정보 입력
for _ in range(m):
    #A번 섬과 B번 섬 사이에 중량제한이 C인 다리가 존재
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    start = min(start,c)
    end = max(end,c)
    
#두 공장의 위치
factory1, factory2 = map(int,input().split())

#이분탐색을 진행한다.
while start <= end:
    mid = (start+end) // 2
    
    #공장1의 위치가 처음 방문하는 곳이다.
    bfs_q.append(factory1)
    visited.add(factory1)
    
    
    while bfs_q:
        pops = bfs_q.popleft()
        visit_q.append(pops)
        
        #방문한 섬의 인접한 섬을 방문한다.
        for k,v in graph[pops].items():
            #이미 방문했으면 또 방문할 필요가 없다.
            if k in visited:
                continue
                
            #만약 중량이 중량제한보다 작을경우 방문할 수 있으므로 방문처리 해준다.
            #만약 중량이 중량제한보다 초과하는 경우 방문할 수 없으므로 방문처리 하지 않는다. 즉 없는노드 취급.
            if v >= mid:
                bfs_q.append(k)
                visited.add(k)
    
    #최종적으로 공장2가 있는 섬을 방문했으면 visited set 안에 공장 2가 있는 섬이 있다.
    #만약 visited set 안에 공장2가 있는 섬이 있을 경우 더 큰 중량으로도 공장2가 있는 섬을
    #방문할 수 있는지 검사하기 위해 이분탐색으로 start에 mid+1을 대입.
    if factory2 in visited:
        start = mid+1
    
    #방문할 수 없는경우 중량을 줄여야하므로 end에 mid-1 대입
    
    else :
        end = mid-1
        
    bfs_q.clear()
    visited.clear()

# 이분탐색이 끝난경우 end값이 공장2가 있는 섬을 방문할 수 있는 최대 중량이다.
print(end)
    