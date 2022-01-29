import sys
from collections import deque

input = sys.stdin.readline

island_num = 2

def bfs(maps,startx,starty):
    global island_num
    dx,dy = [1,-1,0,0,1,1,-1,-1],[0,0,1,-1,-1,1,-1,1]
    q = deque()
    
    q.append((startx,starty))
    maps[startx][starty] = island_num

    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            if nx == -1 or ny == -1 or nx == len(maps) or ny == len(maps[0]):
                continue
            if maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] = island_num

    island_num += 1
    
def solve(w,h):
    maps = []
    for i in range(h):
        maps.append(list(map(int,input().split())))
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 1:
                bfs(maps,i,j)
    
    return max(max(c) for c in maps)

while True:
    w, h = map(int,input().split())
    if w == 0 and h == 0:
        break
    if w == 1 and h == 1:
        if int(input()) == 1:
            print(1)
        else :
            print(0)
    
    else :
        ans = solve(w,h)-1
        print(ans if ans >= 0 else 0)
    island_num = 2