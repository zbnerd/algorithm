import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

def gravity(a, toward):
    goal_red = False
    goal_blue = False
    
    ri, rj, bi, bj = 0, 0, 0, 0
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                ri, rj = i, j
            
            if a[i][j] == 'B':
                bi, bj = i, j
    
    if toward == 0:
        for k in range(n):
            # 빨간구슬
            if not goal_red:
                if a[ri-1][rj] == '.':
                    a[ri-1][rj], a[ri][rj] = 'R', '.'
                    ri -= 1
                    
                if a[ri-1][rj] == 'O':
                    a[ri][rj] = '.'
                    goal_red = True
                
            # 파란구슬
            if not goal_blue:
                if a[bi-1][bj] == '.':
                    a[bi-1][bj], a[bi][bj] = 'B', '.'
                    bi -= 1
                    
                if a[bi-1][bj] == 'O':
                    a[bi][bj] = '.'
                    goal_blue = True
                    
    if toward == 1:
        for k in range(n):
            # 빨간구슬
            if not goal_red:
                if a[ri+1][rj] == '.':
                    a[ri+1][rj], a[ri][rj] = 'R', '.'
                    ri += 1
                    
                if a[ri+1][rj] == 'O':
                    a[ri][rj] = '.'
                    goal_red = True
                
            # 파란구슬
            if not goal_blue:
                if a[bi+1][bj] == '.':
                    a[bi+1][bj], a[bi][bj] = 'B', '.'
                    bi += 1
                    
                if a[bi+1][bj] == 'O':
                    a[bi][bj] = '.'
                    goal_blue = True
                    
    if toward == 2:
        for k in range(m):
            # 빨간구슬
            if not goal_red:
                if a[ri][rj-1] == '.':
                    a[ri][rj-1], a[ri][rj] = 'R', '.'
                    rj -= 1
                    
                if a[ri][rj-1] == 'O':
                    a[ri][rj] = '.'
                    goal_red = True
                
            # 파란구슬
            if not goal_blue:
                if a[bi][bj-1] == '.':
                    a[bi][bj-1], a[bi][bj] = 'B', '.'
                    bj -= 1
                    
                if a[bi][bj-1] == 'O':
                    a[bi][bj] = '.'
                    goal_blue = True
                    
    if toward == 3:
        for k in range(m):
            # 빨간구슬
            if not goal_red:
                if a[ri][rj+1] == '.':
                    a[ri][rj+1], a[ri][rj] = 'R', '.'
                    rj += 1
                    
                if a[ri][rj+1] == 'O':
                    a[ri][rj] = '.'
                    goal_red = True
                
            # 파란구슬
            if not goal_blue:
                if a[bi][bj+1] == '.':
                    a[bi][bj+1], a[bi][bj] = 'B', '.'
                    bj += 1
                    
                if a[bi][bj+1] == 'O':
                    a[bi][bj] = '.'
                    goal_blue = True
    
    return a

def is_exist(a, color):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == color:
                return True
                
    return False
    
def bfs(a):
    
    q = deque()
    q.append((deepcopy(a), -1, 0)) # world, toward, cnt
    
    while q:
        board, toward, cnt = q.popleft()
        
        if not is_exist(board, 'R') and is_exist(board,'B'):
            return cnt
            
        if cnt == 11:
            return -1
        
        for i in range(4):
            if toward != i:
                n_board = gravity(deepcopy(board), i)
                q.append((deepcopy(n_board), i, cnt+1))
        

n, m = map(int, input().split())
world = [list(input()[:-1]) for _ in range(n)]

print(bfs(world))