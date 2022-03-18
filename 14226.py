import sys
from collections import deque

input = sys.stdin.readline

def bfs(S):
    emoji = [[float('inf')] * (S+1) for _ in range(S+1)]

    q = deque()
    q.append((1, 0)) #화면에 있는 이모티콘수, 클립보드에 있는 이모티콘수
    emoji[1][0] = 0 # emoji[화면에 있는 이모티콘수][클립보드에 있는 이모티콘수] = 시간

    while q:
        s, c = q.popleft()
        
        #1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
        if emoji[s][s] == float('inf'):
            emoji[s][s] = emoji[s][c] + 1
            q.append((s, s))

        #2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
        if s + c <= S and emoji[s + c][c] == float('inf'):
            emoji[s + c][c] = emoji[s][c] + 1
            q.append((s + c, c))

        #3. 화면에 있는 이모티콘 중 하나를 삭제한다.
        if  s >= 1 and emoji[s - 1][c] == float('inf'):
            emoji[s - 1][c] = emoji[s][c] + 1
            q.append((s - 1, c))
        

    ans = emoji[S][:(S+1)]

    return min(ans)

S = int(input())
print(bfs(S))