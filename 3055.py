from collections import deque
import sys

input = sys.stdin.readline

#bfs 함수
def bfs(titub_forest):
    
    global row, col

    visited = [[False] * col for _ in range(row)]

    # 방향벡터
    di, dj = [1,-1,0,0], [0,0,1,-1]

    q_hedg = deque()
    q_flood = deque()

    # 고슴도치, 물 초기 좌표
    for i in range(row):
        for j in range(col):
            if titub_forest[i][j] == 'S':
                q_hedg.append((i, j, 0))
                titub_forest[i][j] = '.'
                visited[i][j] = True

            elif titub_forest[i][j] == '*':
                q_flood.append((i, j))
                visited[i][j] = True

            elif titub_forest[i][j] == 'X':
                visited[i][j] = True
    
    while q_hedg:
        # 홍수 일으키기
        for _ in range(len(q_flood)) :
            water_i, water_j = q_flood.popleft()

            for k in range(4):
                ni, nj = water_i+di[k], water_j+dj[k]

                if 0 <= ni < row and 0 <= nj < col:
                    if titub_forest[ni][nj] == '.' and not visited[ni][nj] :
                        titub_forest[ni][nj] = '*'
                        q_flood.append((ni, nj))
                        visited[ni][nj] = True
        
        # 고슴도치 움직이기
        for _ in range(len(q_hedg)):
            hedg_i, hedg_j, t = q_hedg.popleft()

            for k in range(4):
                ni, nj = hedg_i+di[k], hedg_j+dj[k]

                if 0 <= ni < row and 0 <= nj < col:
                    if titub_forest[ni][nj] == '.' and not visited[ni][nj] :
                        titub_forest[ni][nj] = '*'
                        q_hedg.append((ni, nj, t+1))
                        visited[ni][nj] = True

                    if titub_forest[ni][nj] == 'D':
                        return t+1

    return "KAKTUS"

# 티떱숲 크기 입력
row, col = map(int, input().split())

# 티떱숲 정보 입력
titub_forest = [list(input()) for _ in range(row)]
# X : 돌
# D : 비버의 굴
# S : 고슴도치
# * : 물이 차있는 곳

#BFS 실행
print(bfs([item[:] for item in titub_forest]))