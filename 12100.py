from itertools import chain
from copy import deepcopy
import sys

input = sys.stdin.readline

def print2d(a):
    for c in a:
        print(*c)

def get_maxValue_from2d(a):
    return max(list(chain(*a)))

def swift_up(arr):
    
    tmp = deepcopy(arr)

    for k in range(n):
        for i in range(n-1):
            for j in range(n):
                if tmp[i][j] == 0 and tmp[i+1][j] != 0:
                    tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]
                    

    for k in range(n):
        for i in range(1,n):
            for j in range(n):
                if tmp[i-1][j] == 0 and tmp[i][j] != 0:
                    tmp[i-1][j], tmp[i][j] = tmp[i][j], tmp[i-1][j]

                        
    for i in range(n-1):
        for j in range(n):
            if tmp[i][j] == tmp[i+1][j]:
                tmp[i][j], tmp[i+1][j] = 2*tmp[i][j], 0

    for k in range(n):
        for i in range(n-1):
            for j in range(n):
                if tmp[i][j] == 0 and tmp[i+1][j] != 0:
                    tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]
                    

    for k in range(n):
        for i in range(1,n):
            for j in range(n):
                if tmp[i-1][j] == 0 and tmp[i][j] != 0:
                    tmp[i-1][j], tmp[i][j] = tmp[i][j], tmp[i-1][j]
                                        

    return tmp

def swift_down(arr):
    
    tmp = deepcopy(arr)

    for k in range(n):
        for i in range(n-1):
            for j in range(n):
                if tmp[i][j] != 0 and tmp[i+1][j] == 0:
                    tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]

    for k in range(n):
        for i in range(1,n):
            for j in range(n):
                if tmp[i-1][j] != 0 and tmp[i][j] == 0:
                    tmp[i-1][j], tmp[i][j] = tmp[i][j], tmp[i-1][j]
                    
    for i in range(n-1,0,-1):
        for j in range(n):
            if tmp[i-1][j] == tmp[i][j]:
                tmp[i-1][j], tmp[i][j] = 0, 2*tmp[i][j]

    for k in range(n):
        for i in range(n-1):
            for j in range(n):
                if tmp[i][j] != 0 and tmp[i+1][j] == 0:
                    tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i][j]

    for k in range(n):
        for i in range(1,n):
            for j in range(n):
                if tmp[i-1][j] != 0 and tmp[i][j] == 0:
                    tmp[i-1][j], tmp[i][j] = tmp[i][j], tmp[i-1][j]

            
    return tmp
    
def swift_left(arr):
    
    tmp = deepcopy(arr)
    
    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tmp[i][j] == 0 and tmp[i][j+1] != 0:
                    tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(1,n):
                if tmp[i][j-1] == 0 and tmp[i][j] != 0:
                    tmp[i][j-1], tmp[i][j] = tmp[i][j], tmp[i][j-1]

    for i in range(n):
        for j in range(n-1):
            if tmp[i][j] == tmp[i][j+1]:
                tmp[i][j], tmp[i][j+1] = 2*tmp[i][j], 0

    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tmp[i][j] == 0 and tmp[i][j+1] != 0:
                    tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(1,n):
                if tmp[i][j-1] == 0 and tmp[i][j] != 0:
                    tmp[i][j-1], tmp[i][j] = tmp[i][j], tmp[i][j-1]

    
    return tmp
    
def swift_right(arr):
    
    tmp = deepcopy(arr)

    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tmp[i][j] != 0 and tmp[i][j+1] == 0:
                    tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(1,n):
                if tmp[i][j-1] != 0 and tmp[i][j] == 0:
                    tmp[i][j-1], tmp[i][j] = tmp[i][j], tmp[i][j-1]
                    
    for i in range(n):
        for j in range(n-1,0,-1):
            if tmp[i][j-1] == tmp[i][j]:
                tmp[i][j-1], tmp[i][j] = 0, 2*tmp[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n-1):
                if tmp[i][j] != 0 and tmp[i][j+1] == 0:
                    tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(1,n):
                if tmp[i][j-1] != 0 and tmp[i][j] == 0:
                    tmp[i][j-1], tmp[i][j] = tmp[i][j], tmp[i][j-1]


    return tmp

        
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

max_value = 0

for i in range(2**10):
    bit = bin(i)[2:].zfill(10)
    board_tmp = deepcopy(board)
    
    cmd = []
    for j in range(0,10,2):
        cmd.append(int(bit[j])*2+int(bit[j+1]))
        
    for c in cmd:
        if c == 0: #up
            board_tmp = swift_up(board_tmp)
            
        if c == 1: #down
            board_tmp = swift_down(board_tmp)
            
        if c == 2: #left
            board_tmp = swift_left(board_tmp)
            
        if c == 3: #right
            board_tmp = swift_right(board_tmp)
        
        
            
    max_value = max(max_value,get_maxValue_from2d(board_tmp))

print(max_value)