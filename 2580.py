from itertools import chain, permutations
from collections import defaultdict
import sys

input = sys.stdin.readline

#2차원 출력
def print2d(a):
    for c in a:
        print(*c)

#2차원 리스트를 1차원 리스트로 만듦
def reshape_2d_to_1d(a):
    return list(chain(*a))

#가로줄 추출
def export_horizental(b,i):
    return b[i]

#세로줄 추출
def export_vertical(b,i):
    return [v[i] for v in b]

#3x3 추출
def export_3x3(b,i,j):
    j //= 3
    i //= 3

    j *= 3
    i *= 3

    return [row[j:j+3] for row in b[i:i+3]]

#후보값 집합 추출
def candidate_num(x,y):

    universal_num = {1,2,3,4,5,6,7,8,9}

    square = set(reshape_2d_to_1d(export_3x3(board, x, y)))-{0}
    horizen = set(export_horizental(board, x))-{0}
    vertical = set(export_vertical(board, y))-{0}

    return universal_num - square - horizen - vertical

#깊이우선탐색
def dfs(x):
    # 모든 빈칸이 채워진경우 출력후 종료
    if x == len(blank_coords) :
        print2d(board)
        sys.exit(0)

    #후보값 집합 추출
    candidate = candidate_num(blank_coords[x][0], blank_coords[x][1])
    
    #후보값 집합을 토대로 dfs
    for n in candidate:
        board[blank_coords[x][0]][blank_coords[x][1]] = n
        dfs(x+1)
        board[blank_coords[x][0]][blank_coords[x][1]] = 0

#스도쿠 보드 입력
board = [list(map(int, input().split())) for _ in range(9)]

#빈 좌표들 추출
blank_coords = []

for i in range(0,9,3):
    for j in range(0,9,3):
        
        list33 = export_3x3(board,i,j)
        #빈좌표 추가
        for a in range(3):
            for b in range(3):
                if list33[a][b] == 0:
                    blank_coords.append((a+i,b+j))

#DFS
dfs(0)