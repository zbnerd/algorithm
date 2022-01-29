import sys
from collections import deque

def bfs(sx,sy,ex,ey,I):
    dx, dy = [1,1,2,2,-1,-1,-2,-2],[2,-2,1,-1,2,-2,1,-1]

    q = deque()
    visited = set()
    
    q.append((sx,sy,0))
    visited.add((sx,sy))

    while q:
        x, y, move_cnt = q.popleft()

        if x == ex and y == ey:
            return move_cnt

        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= I or ny >= I:
                continue
            if (nx, ny) not in visited:
                q.append((nx, ny, move_cnt+1))
                visited.add((nx,ny))
                
def solve():
    I = int(input())
    startx, starty = map(int,input().split())
    endx, endy = map(int,input().split())
    print(bfs(startx,starty,endx,endy,I))
    
for _ in range(int(input())):
    solve()
