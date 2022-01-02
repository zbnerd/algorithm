import sys
from collections import defaultdict
import heapq
import math

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, start):
    
    distances = {node: math.inf for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if distances[current_node] < current_distance:
            continue
            
        for adjacent in graph[current_node]:
            distance = current_distance + adjacent[1]
            
            if distance < distances[adjacent[0]]:
                distances[adjacent[0]] = distance
                heapq.heappush(queue, [distance, adjacent[0]])
                
    return distances

v,e = map(int, input().split())
start = int(input())

graph = defaultdict(list)

for i in range(e):
    f,t,w = map(int, input().split())
    graph[f].append((t,w))
    
for i in range(1,v+1):
    if i not in graph:
        graph[i].append((1,math.inf))

dij_graph = dijkstra(graph,start)

for v in range(v):
    print("INF" if dij_graph[v+1]==math.inf else dij_graph[v+1])
