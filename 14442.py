from collections import deque
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
maps = [list(map(int, list(input()[:-1]))) for _ in range(n)]

def bfs(maps):

    global k

    di, dj = [0,0,1,-1], [1,-1,0,0]

    q = deque()
    visited = [[False] * m for _ in range(n)]
    visited3d = []

    for _ in range(12):
        visited3d.append([item[:] for item in visited])
    
    q.append((0,0,0,1)) # y, x, 부순 벽의 갯수, 거리
    visited3d[0][0][0] = True

    while q:
        i, j, ck, dist = q.popleft()

        if i == n-1 and j == m-1:
            return dist

        for a in range(4):
            ni, nj = i+di[a], j+dj[a]

            if 0 <= ni < n and 0 <= nj < m:
                # 빈칸 이동하는 경우
                if not visited3d[ck][ni][nj] and maps[ni][nj] == 0:
                    q.append((ni, nj, ck, dist+1))
                    visited3d[ck][ni][nj] = True

                # 벽을 부수고 이동하는 경우
                if not visited3d[ck+1][ni][nj] and maps[ni][nj] == 1 and ck < k:
                    q.append((ni, nj, ck+1, dist+1))
                    visited3d[ck+1][ni][nj] = True


    return -1

print(bfs([item[:] for item in maps]))