import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def solve():
    p = deque(list(input()[:-1]))
    n = int(input())
    n_list = deque(input()[1:-2].split(','))
    tmp = deque()
    Rev = False
    empty = False
    
    error = False
    
    while p:
        cmd = p.popleft()
        
        if cmd == 'R':
            Rev = not Rev
        
        elif cmd == 'D':
            if len(n_list) == 0:
                error = True
                break
            elif n == 0:
                error = True
                break
                
            else :
                try:
                    if Rev :
                        n_list.pop()
                    else :
                        n_list.popleft()
                except:
                    error = True
                    break
    
    if error:
        print('error')
    else:
        print('[',end='')
        for i in range(len(n_list)):
            if Rev:
                print(n_list[-i-1],end='')
            else:
                print(n_list[i],end='')
            
            if i < len(n_list)-1:
                print(',',end='')
        print(']')
        

for _ in range(int(input())):
    solve()