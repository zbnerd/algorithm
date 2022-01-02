# 1916 최소비용 구하기
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input()) #도시의 수
m = int(input()) #버스의 수

graph = defaultdict(list)
load = defaultdict(int)

def dijkstra(start,end):
    distances = {i:float('inf') for i in graph.keys()}
    distances[start] = 0
    path = []
    
    heap = []
    
    heapq.heappush(heap,(distances[start],start))
    
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        
        if distances[current_node] < current_dist:
            continue
            
        for adj in graph[current_node]:
            dist = current_dist + adj[1]
            
            if dist < distances[adj[0]]:
                distances[adj[0]] = dist
                load[adj[0]] = current_node
                heapq.heappush(heap, (dist,adj[0]))
                
    
    path_part = end
    
    while path_part != start:
        path.append(path_part)
        path_part = load[path_part]
        
    path.append(start)        
    path.reverse()
    
    return distances[end], path

for _ in range(m):
    a,b,c = map(int,input().split()) #a도시에서 b도시로 가는 버스 요금이 c
    graph[a].append((b,c))
    
for i in range(1,n+1):
    if i not in graph:
        graph[i].append((1,float('inf')))
    
s,e = map(int,input().split())

mincost, path = dijkstra(s,e)
print(mincost)
print(len(path))
print(*path)
