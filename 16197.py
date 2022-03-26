from collections import deque
import sys

input = sys.stdin.readline

def bfs(coin):
    coin1 = coin[0]
    coin2 = coin[1]

    di, dj = [1,-1,0,0], [0,0,1,-1]

    q = deque()
    q.append((coin1[0], coin1[1], coin2[0], coin2[1], 0))

    while q:
        i1, j1, i2, j2, push_btn = q.popleft()


        if push_btn < 10:
            for k in range(4):
                ni1, nj1, ni2, nj2 = i1+di[k], j1+dj[k], i2+di[k], j2+dj[k]
                
                #범위 내인경우
                if (0 <= ni1 < n and 0 <= nj1 < m) and (0 <= ni2 < n and 0 <= nj2 < m):
                    next_position = []

                    #벽인경우
                    if board[ni1][nj1] == '#':
                        next_position.append(i1)
                        next_position.append(j1)

                    #벽이 아닌경우
                    elif board[ni1][nj1] == '.' or board[ni1][nj1] == 'o':
                        next_position.append(ni1)
                        next_position.append(nj1)

                    #벽인경우
                    if board[ni2][nj2] == '#':
                        next_position.append(i2)
                        next_position.append(j2)

                    #벽이 아닌경우
                    elif board[ni2][nj2] == '.' or board[ni2][nj2] == 'o':
                        next_position.append(ni2)
                        next_position.append(nj2)

                    next_position.append(push_btn+1)
                    q.append(next_position)

                #범위 내가 아닌 경우
                #동전 1이 떨어지는 경우
                elif (not (0 <= ni1 < n and 0 <= nj1 < m)) and (0 <= ni2 < n and 0 <= nj2 < m):
                    print(push_btn+1)
                    return
                
                #동전 2가 떨어지는 경우
                elif (0 <= ni1 < n and 0 <= nj1 < m) and (not (0 <= ni2 < n and 0 <= nj2 < m)):
                    print(push_btn+1)
                    return

                #둘다 떨어지는 경우
                else :
                    continue

    print(-1)
    
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

coin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            coin.append((i,j))

bfs(coin)