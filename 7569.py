#7569 토마토
import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int,input().split())
#m 가로 #n 세로 h 층수
dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]

q = deque()

tomato_box = []
for f in range(h):
    box = []
    for i in range(n):
        box.append(list(map(int,input().split())))
    tomato_box.append(box)

zero_cnt = 0
#0이 있는지 검사
for i in range(len(tomato_box)):
    for j in range(len(tomato_box[i])):
        for k in range(len(tomato_box[i][j])):
            if tomato_box[i][j][k] == 0:
                zero_cnt += 1
                
if zero_cnt == 0: #안익은 토마토가 없는 경우
    #모든 원소값의 합 추출
    sigma = 0
    for i in range(len(tomato_box)):
        for j in range(len(tomato_box[i])):
            sigma += sum(tomato_box[i][j])
            
    if sigma == (-m*n*h):
        print(-1)
    else:
        print(0)
        
else: #그외
    #[h][y][x]
    for i in range(len(tomato_box)):
        for j in range(len(tomato_box[i])):
            for k in range(len(tomato_box[i][j])):
                if tomato_box[i][j][k] == 1:
                    q.append((i,j,k))
                    
    while q:
        z,y,x = q.popleft()
        
        for i in range(6):
            nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
            if nx == -1 or ny == -1 or nz == -1:
                continue
            if nx == m or ny == n or nz == h:
                continue
            
            if tomato_box[nz][ny][nx] != -1 and tomato_box[nz][ny][nx] == 0:
                tomato_box[nz][ny][nx] = tomato_box[z][y][x] + 1
                q.append((nz,ny,nx))
                
    zero = sum(sum(x.count(0) for x in y) for y in tomato_box)
    if zero:
        print(-1)
    else:
        maxi = 0
        for i in range(len(tomato_box)):
            for j in range(len(tomato_box[i])):
                for k in range(len(tomato_box[i][j])):
                    maxi = max(maxi,tomato_box[i][j][k])
                    
        print(maxi-1)

