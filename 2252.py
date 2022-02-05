from collections import deque, defaultdict
import sys

n, m = map(int,input().split())
def topology_sort():
    q = deque()
    topology_sorted = []

    for i in range(1,n+1):
        if in_degree[i] == 0:
            q.append(i)

    for i in range(1,n+1):
        if not q:
            return
        
        pop = q.popleft()
        for adj in graph[pop]:
            in_degree[adj] -= 1

            if in_degree[adj] == 0:
                q.append(adj)

        topology_sorted.append(pop)

    return topology_sorted

graph = defaultdict(list)
in_degree = [0 for i in range(n+1)]

for _ in range(m):
    f, t = map(int,input().split())
    graph[f].append(t)
    in_degree[t] += 1

print(*topology_sort())