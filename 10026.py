#10026 적록색약
import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

def test_print(arr):
    for c in arr:
        print(*c)

def flood_fill(paper,target,x,y):
    if paper[x][y] != target:
        return
    paper[x][y] = 'V'
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if nx == -1 or ny == -1 or nx == len(paper) or ny == len(paper):
            continue
        flood_fill(paper,target,nx,ny)
        
dx,dy = [1,-1,0,0],[0,0,1,-1]
color = ['R','G','B']
paper = []
cw_paper = []
q = deque()

#종이와 색약종이 입력
for _ in range(int(input())):
    col = input()[:-1]
    paper.append(list(col))
    cw_paper.append(list(col))
    
#색약 색종이 RG색약 적용 - BFS
for i in range(len(cw_paper)):
    for j in range(len(cw_paper[i])):
        if cw_paper[i][j] == 'R':
            q.append((i,j))
            
while q:
    x,y = q.popleft()
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx == -1 or ny == -1 or nx == len(cw_paper) or ny == len(cw_paper):
            continue
        if cw_paper[nx][ny] == 'G':
            cw_paper[nx][ny] = 'R'
            q.append((nx,ny))
        
nomality, color_weakness = 0,0

#정상인 색종이 영역수 구하기

for i in range(len(paper)):
    for j in range(len(paper[i])):
        #영역수 구하기
        for k in range(3):
            if paper[i][j]==color[k]:
                nomality += 1
                flood_fill(paper,color[k],i,j)

            if cw_paper[i][j]==color[k]:
                color_weakness += 1
                flood_fill(cw_paper,color[k],i,j)
        
            
print(nomality,color_weakness)