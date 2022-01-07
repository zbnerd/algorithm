# 10282 해킹
import sys
from collections import defaultdict
import heapq

def dijkstra(graph,start,n):
    
    path = defaultdict(int)
    
    distances = defaultdict(int)
    
    for i in range(1,n+1):
        distances[i] = sys.maxsize
    
    distances[start] = 0
    
    heap = [(distances[start],start)]
    last_node = 0
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > distances[cur_node]:
            continue
        
        for adj_node, adj_dist in graph[cur_node]:
            accum_dist = cur_dist + adj_dist
            if accum_dist < distances[adj_node]:
                distances[adj_node] = accum_dist
                path[adj_node] = cur_node
                heapq.heappush(heap,(accum_dist,adj_node))
                
    _max = 0
    cnt = 0
    for i in distances.values():
        if i != sys.maxsize:
            _max = max(i,_max)
            cnt+=1
        
    
    return cnt,_max
    
    
def solve():
    n,d,c = map(int,input().split())
    graph = defaultdict(list)
    
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    
    for i in range(n+1):
        if i not in graph:
            graph[i].append((1,sys.maxsize))
    
    print(*dijkstra(graph,c,n))
    

for _ in range(int(input())):
    solve()