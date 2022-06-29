from collections import deque
import sys

input = sys.stdin.readline

w, h = map(int, input().split())
maps = [list(input()[:-1]) for _ in range(h)]

def bfs(maps):

    mirror_count = [[float('inf')] * w for _ in range(h)]

    q = deque()
    c_q = deque()

    di, dj = [0,0,1,-1], [1,-1,0,0] #right, left, down, up

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'C':
                c_q.append((i,j))
                
    visited = [[False] * w for _ in range(h)]

    start = c_q.pop()
    mirror_count[start[0]][start[1]] = -1
    end = c_q.pop()

    # 레이저 포인트에서 4방향으로 발사
    for k in range(4):
        

        for m in range(max(w,h)):
            ni, nj = start[0]+di[k]*(m+1), start[1]+dj[k]*(m+1)
            if 0 <= ni < h and 0 <= nj < w:
                if maps[ni][nj] == '*':
                    break
                
                mirror_count[ni][nj] = 0
                q.append((ni, nj, k, 0)) #y좌표, x좌표, 방향, 사용된 거울 갯수
                visited[ni][nj] = True

    while q:
        i, j, arrow, cur_mirror_cnt = q.popleft()

        # 레이저가 오른쪽 방향으로 진행한 경우
        if arrow == 0:
            # 슬래시 거울 : 위로
            for k in range(h):
                ni, nj = i-1-k, j

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 3, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

            # 역슬래시 거울 : 아래로
            for k in range(h):
                ni, nj = i+1+k, j

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 2, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break


        # 레이저가 왼쪽 방향으로 진행한 경우
        if arrow == 1:
            # 슬래시 거울 : 아래로
            for k in range(h):
                ni, nj = i+1+k, j

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 2, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

            # 역슬래시 거울 : 위로
            for k in range(h):
                ni, nj = i-1-k, j

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 3, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

        # 레이저가 아래쪽 방향으로 진행한 경우
        if arrow == 2:
            # 슬래시 거울 : 왼쪽으로
            for k in range(w):
                ni, nj = i, j-1-k

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 1, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

            # 역슬래시 거울 : 오른쪽으로
            for k in range(h):
                ni, nj = i, j+1+k

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 0, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

        # 레이저가 위쪽 방향으로 진행한 경우
        if arrow == 3:
            # 슬래시 거울 : 오른쪽으로
            for k in range(w):
                ni, nj = i, j+1+k

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 0, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

            # 역슬래시 거울 : 왼쪽으로
            for k in range(h):
                ni, nj = i, j-1-k

                if 0 <= ni < h and 0 <= nj < w:
                    try :
                        if maps[ni][nj] == '*':
                            break

                        if mirror_count[ni][nj] > cur_mirror_cnt and not visited[ni][nj]:
                            mirror_count[ni][nj] = cur_mirror_cnt+1
                            q.append((ni, nj, 1, cur_mirror_cnt+1))
                            visited[ni][nj] = True
                    
                    except : break

    return mirror_count[end[0]][end[1]]
                        
print(bfs(maps))