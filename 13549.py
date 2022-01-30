from collections import deque
import sys

input = sys.stdin.readline

def bfs(n, k):
    
    q = deque()
    cost = [99999999] * 400002
    
    q.append((n,0))
    cost[n] = 0

    while q:
        dist, sec = q.popleft()

        forward = dist+1
        backward = dist-1
        teleport = 2*dist

        if forward <= 400001:
            if cost[dist] + 1 < cost[forward]:
                q.append((forward, sec+1))
                cost[forward] = min(cost[forward],cost[dist] + 1)

        if backward >= 0:
            if cost[dist] + 1 < cost[backward]:
                q.append((backward, sec+1))
                cost[backward] = min(cost[backward],cost[dist] + 1)

        if teleport <= 400001:
            if cost[dist] < cost[teleport]:
                q.appendleft((teleport, sec))
                cost[teleport] = min(cost[teleport],cost[dist])
                
    return cost[k]

                
def solve():
    n, k = map(int,input().split())
    print(bfs(n, k))
    
solve()