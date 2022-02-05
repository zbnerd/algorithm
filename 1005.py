from collections import deque, defaultdict
import sys

input = sys.stdin.readline

def topology_sort(graph, in_degree, D, w):
    DP = [0 for i in range(len(in_degree))]

    q = deque()
    for i in range(1,len(in_degree)):
        if in_degree[i] == 0:
            q.append(i) #element
            DP[i] = D[i]

    while q:
        element = q.popleft()

        for adj in graph[element]:
            in_degree[adj] -= 1
            DP[adj] = max(DP[adj],D[adj]+DP[element])

            if in_degree[adj] == 0:
                q.append(adj)
                

    return DP


def solve():
    n, k = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    topology_set = set()

    graph = defaultdict(list)
    in_degree = [0 for n in range(n+1)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1
        topology_set.add(x)
        topology_set.add(y)

    w = int(input())
    
    if w not in topology_set: print(D[w])
    else: print(topology_sort(graph, in_degree, D, w)[w])

for _ in range(int(input())):
    solve()