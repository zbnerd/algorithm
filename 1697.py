import sys
from collections import deque

input = sys.stdin.readline
visited = set()
bfs_q = deque()

n,k = map(int, input().split())
bfs_q.append((n,0)) # n,depth
visited.add(n)

while deque:
    pop_val, depth = bfs_q.popleft()
    if pop_val == k:
        print(depth)
        break
    
    else :
        if pop_val < 100000:
            if pop_val+1 not in visited:
                bfs_q.append((pop_val+1,depth+1))
                visited.add(pop_val+1)
                    
        if pop_val <= 50000:
            if pop_val*2 not in visited:
                bfs_q.append((pop_val*2,depth+1))
                visited.add(pop_val*2)
                
        if pop_val > 0:
            if pop_val-1 not in visited:
                bfs_q.append((pop_val-1,depth+1))
                visited.add(pop_val-1)
        