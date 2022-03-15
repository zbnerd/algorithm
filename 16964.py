from collections import defaultdict
import sys

input = sys.stdin.readline

def dfs(n):

    dfs_result.append(n)

    for adj in graph[n]:
        if adj not in visited:
            visited.add(adj)
            dfs(adj)
            
def is_equall(a,b):
    for i in range(n):
        if a[i] != b[i]:
            return False

    return True

def orders(a):
    return order[a]

n = int(input())

visited = set()
dfs_result = []
graph = defaultdict(list)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

input_dfsOrder = list(map(int, input().split()))
order = [0] * 100001

if input_dfsOrder[0] != 1:
    print(0)
    exit()

for i in range(n):
    order[input_dfsOrder[i]] = i+1

for v in graph.values():
    v.sort(key = orders)

visited.add(input_dfsOrder[0])
dfs(input_dfsOrder[0])
print(1 if is_equall(input_dfsOrder, dfs_result) else 0)