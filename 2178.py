import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
maze = []
dx, dy = [0,0,1,-1],[1,-1,0,0] #4방향 탐색
q = deque()

#미로 입력
maze.append([0]*(m+2))

for i in range(n):
    maze.append([0]+list(map(int,list(input()[:-1])))+[0])
    
maze.append([0]*(m+2))

#시작지점 큐에 삽입
q.append((1,1))
maze[1][1] = 2

#BFS

while q:
    x,y = q.popleft()
    
    #인접한곳 탐색
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y]+1
            q.append((nx,ny))

print(maze[n][m]-1)
