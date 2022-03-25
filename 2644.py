from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def bfs(s):
    visited = set()
    q = deque()

    q.append((s,0))
    visited.add(s)

    while q:
        pop, cnt = q.popleft()

        if pop == p2:
            print(cnt)
            return

        for v in graph[pop]:
            if v not in visited:
                visited.add(v)
                q.append((v,cnt+1))

    print(-1)
    
n = int(input())
p1, p2 = map(int, input().split())

graph = defaultdict(list)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs(p1)