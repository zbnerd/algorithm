from collections import defaultdict
import heapq as hq
import sys

input = sys.stdin.readline

def topology_sort(graph):
    pq = []
    t_sort = []
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            hq.heappush(pq,i)
        
    while pq:
        pop = hq.heappop(pq)
        t_sort.append(pop)

        for e in graph[pop]:
            in_degree[e] -= 1
            if in_degree[e] == 0:
                hq.heappush(pq,e)

    return t_sort[1:]

n,m = map(int,input().split())
graph = defaultdict(list)
in_degree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    in_degree[b]+=1
    
print(*topology_sort(graph))