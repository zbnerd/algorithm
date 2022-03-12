def dfs(x, y, color, depth):
    #이미 방문한경우 리턴
    if visited[x][y]:
        return abs(depth-dist[x][y]) >= 4

    #방문처리
    visited[x][y] = True
    dist[x][y] = depth
    
    dx, dy = [1,-1,0,0], [0,0,1,-1]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if color == board[nx][ny]:
                if dfs(nx, ny, color, depth+1):
                    return True

    return False

def isvaild(v):
    for c in v:
        if c:
            return True

    return False

#입력
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

vaild = []
visited = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
#시작지점을 i, j로 하기위한 반복문
for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        vaild.append(dfs(i,j,board[i][j],1))

print('Yes' if isvaild(vaild) else 'No')