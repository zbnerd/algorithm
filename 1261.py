from collections import deque
import sys

input = sys.stdin.readline

def zero_one_BFS(maze):
    # 방향벡터
    di, dj = [1,-1,0,0],[0,0,1,-1]

    # 방문처리를 위한 배열
    visited = [[False] * len(maze[0]) for _ in range(len(maze))]

    # 0-1 BFS를 위한 덱 선언
    deq = deque()
    deq.append((0,0,0)) #i, j, 뚫린 벽의 갯수
    visited[0][0] = True

    while deq:
        i, j, broken = deq.popleft()

        #n, m에 도착하면 출력하고 0-1 BFS 종료
        if i+1 == len(maze) and j+1 == len(maze[0]):
            print(broken)
            break

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            # 인접 정점이 배열 범위를 벗어나면 수행 안함
            if not (0 <= ni < len(maze) and 0 <= nj < len(maze[0])):
                continue

            # 인접 정점이 이미 방문한 경우면 수행 안함
            if visited[ni][nj]:
                continue

            #인접 정점 방문처리
            visited[ni][nj] = True
            
            # 인접 정점이 벽을 뚫지 않아도 지나갈 수 있는 경우
            if maze[ni][nj] == 0:
                deq.appendleft((ni,nj,broken))

            # 인접 정점이 벽을 뚫어야 지나갈 수 있는 경우
            else :
                deq.append((ni,nj,broken+1))

m, n = map(int, input()[:-1].split())
zero_one_BFS([list(map(int, list(input()[:-1]))) for _ in range(n)])