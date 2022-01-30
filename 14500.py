import sys

input = sys.stdin.readline

tetromino = dict()

tetromino[0] = {'dx':[0,1,2,3], 'dy':[0,0,0,0]}
tetromino[1] = {'dx':[0,0,0,0], 'dy':[0,1,2,3]}
tetromino[2] = {'dx':[0,1,0,0], 'dy':[0,0,1,2]} 
tetromino[3] = {'dx':[0,0,0,1], 'dy':[0,1,2,2]} 
tetromino[4] = {'dx':[0,1,1,1], 'dy':[0,0,1,2]} 
tetromino[5] = {'dx':[0,1,1,1], 'dy':[2,2,1,0]} 
tetromino[6] = {'dx':[0,0,1,2], 'dy':[0,1,0,0]} 
tetromino[7] = {'dx':[0,0,1,2], 'dy':[0,1,1,1]} 
tetromino[8] = {'dx':[0,1,2,2], 'dy':[0,0,0,1]}
tetromino[9] = {'dx':[0,1,2,2], 'dy':[1,1,1,0]}
tetromino[10] = {'dx':[0,0,1,1], 'dy':[0,1,1,2]}
tetromino[11] = {'dx':[0,0,1,1], 'dy':[1,2,0,1]}
tetromino[12] = {'dx':[0,1,1,2], 'dy':[0,0,1,1]}
tetromino[13] = {'dx':[0,1,1,2], 'dy':[1,0,1,0]}
tetromino[14] = {'dx':[0,0,0,1], 'dy':[0,1,2,1]}
tetromino[15] = {'dx':[0,1,1,1], 'dy':[1,0,1,2]}
tetromino[16] = {'dx':[0,1,1,2], 'dy':[1,0,1,1]}
tetromino[17] = {'dx':[0,1,2,1], 'dy':[0,0,0,1]}
tetromino[18] = {'dx':[0,0,1,1], 'dy':[0,1,0,1]}

n,m = map(int,input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())))
    
total = 0
for t in range(19):
    for i in range(len(board)):
        for j in range(len(board[i])):
            #i,j - 기준점
            tmp = 0
            for k in range(4):
                ni, nj = i+tetromino[t]['dx'][k], j+tetromino[t]['dy'][k]
                try:
                    tmp += board[ni][nj]
                except:
                    tmp = 0
            total = max(total,tmp)

print(total)