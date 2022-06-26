from collections import deque
import sys

input = sys.stdin.readline

#8x8 chess board
board = [list(input()[:-1]) for _ in range(8)]
visited = [[False]*8 for _ in range(8)]

#bfs function
def bfs(board):
    #방향벡터
    di, dj = (0,0,0,1,-1,1,1,-1,-1), (0,1,-1,0,0,1,-1,1,-1)

    visited = set()

    #좌표 bfs 큐
    q = deque()
    q.append((7,0))

    #벽 bfs 큐
    q_wall = deque()
    for i in range(8):
        for j in range(8):
            if board[i][j] == '#':
                q_wall.append((i,j))

    while q:
        
        for _ in range(len(q)):
            i, j = q.popleft()

            if board[i][j] == '#':
                continue

            if i == 0 and j == 7:
                return 1

            for k in range(9):
                ni, nj = i+di[k], j+dj[k]
                    
                if 0 <= ni < 8 and 0 <= nj < 8:
                    if board[ni][nj] == '.' and not (ni, nj) in visited:
                        q.append((ni, nj))
                        visited.add((ni, nj))

        if q_wall:
            visited = set()

        board.pop()
        board.insert(0,['.','.','.','.','.','.','.','.'])

    return 0

#activate bfs and print 1 or 0
print(bfs([item[:] for item in board]))