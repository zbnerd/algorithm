import sys
from itertools import permutations, chain, product
input = sys.stdin.readline

def print2d(a):
    for c in a:
        print(''.join(map(str,c)))
        
def get_vertical(arr, i):
    return set([j[i] for j in arr])

def get_horizontal(arr, i):
    return set(arr[i])
    
def get3x3(arr, i, j):
    j //= 3
    i //= 3
    
    j *= 3
    i *= 3
    
    t = [row[j:j+3] for row in arr[i:i+3]]
    
    return set(chain(*t))

def in_bound(y,x):
    return 0 <= y < 9 and 0 <= x < 9

def back_tracking(count):
    
    global a, terminated
    
    if count == 0:
        if not terminated:
            print("Puzzle",a)
            print2d(board)
            a+=1
            terminated = True
        return
    
    y, x = 0,0
    
    for coord in blank:
        if not board[coord[0]][coord[1]]:
            y, x = coord
            break
    
    promising_c = (u_num - get_vertical(board, x))
    promising_c -= get_horizontal(board, y)
    promising_c -= get3x3(board, y, x)
    
    for cvalue in promising_c:
        for k in range(4):    
            ay, ax = y+dy[k], x+dx[k]
            if in_bound(ay, ax):
                if board[ay][ax] == 0:
                    promising_r = (u_num - get_vertical(board, ax))
                    promising_r -= get_horizontal(board, ay)
                    promising_r -= get3x3(board, ay, ax)
                    
                    for rvalue in promising_r:
                        if cvalue == rvalue: continue
                        if domino[rvalue][cvalue] and domino[cvalue][rvalue]: continue
                        
                        board[y][x] = cvalue
                        board[ay][ax] = rvalue
                        domino[rvalue][cvalue] = True
                        domino[cvalue][rvalue] = True
                        
                        back_tracking(count-2)
                        
                        board[y][x] = 0
                        board[ay][ax] = 0
                        domino[cvalue][rvalue] = False
                        domino[rvalue][cvalue] = False
                        
dy, dx = [1,-1,0,0], [0,0,1,-1]
u_num = {1,2,3,4,5,6,7,8,9}
a = 1

terminated = False

while True:
    n = int(input())
    if n == 0: sys.exit(0)
    
    terminated = False
    
    strings = []
    board = [[0]*9 for _ in range(9)]    


    domino = [[False]*10 for _ in range(10)]

    for _ in range(n):
            
        u, lu, v, lv = input()[:-1].split()
        u, v = int(u), int(v)
        iu, ju = ord(lu[0])-65, int(lu[1])-1
        iv, jv = ord(lv[0])-65, int(lv[1])-1
        board[iu][ju] = u
        board[iv][jv] = v
        
        domino[u][v] = True
        domino[v][u] = True
        
    nums = input()[:-1].split()
    
    for k in range(len(nums)):
        i, j = ord(nums[k][0])-65, int(nums[k][1])-1
        board[i][j] = k+1
    
    blank = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                blank.add((i,j))
    
    blank = list(blank)
    blank.sort()
    count_blank = len(blank)
    
    back_tracking(count_blank)
    
    