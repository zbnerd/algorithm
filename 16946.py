import sys
from collections import deque

input = sys.stdin.readline
        
def print2d(a):
    for c in a:
        strc = list(map(str, c))
        print(''.join(strc))

def bfs(start_coord):
    q = deque()
    si,sj = start_coord
    adj_wall_list = set()
    area = 1
        
    q.append(start_coord)
    
    #방문처리 = -1
    world[si][sj] = -1
    
    while q:
        ci, cj = q.popleft()
        
        for k in range(4):
            ai, aj = ci+di[k], cj+dj[k]
            
            if 0 <= ai < n and 0 <= aj < m:
                if world[ai][aj] == 0:
                    world[ai][aj] = -1
                    q.append((ai,aj))
                    area += 1    
                
                elif world[ai][aj] > 0:
                    adj_wall_list.add((ai,aj))
                    
    for adj_coord in adj_wall_list:
        i, j = adj_coord
        world[i][j] += area
    
            
di, dj = [1,-1,0,0], [0,0,1,-1]

n,m = map(int, input().split())

world = [list(map(int, list(input()[:-1]))) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if world[i][j] == 0:
            bfs((i,j))
            
for i in range(n):
    for j in range(m):
        if world[i][j] == -1:
            world[i][j] = 0
        
        elif world[i][j] > 0:
            world[i][j] %= 10
        
print2d(world)