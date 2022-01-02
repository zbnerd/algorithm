# 1916 최소비용 구하기
import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input()) #도시의 수
m = int(input()) #버스의 수

graph = defaultdict(list)


def dijkstra(start,end):
    distances = {i:float('inf') for i in graph.keys()}
    distances[start] = 0
    
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
                heapq.heappush(heap, (dist,adj[0]))
                
    return distances[end]

for _ in range(m):
    a,b,c = map(int,input().split()) #a도시에서 b도시로 가는 버스 요금이 c
    graph[a].append((b,c))
    
for i in range(1,n+1):
    if i not in graph:
        graph[i].append((1,float('inf')))
    
s,e = map(int,input().split())
print(dijkstra(s,e))
