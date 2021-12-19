import sys

input = sys.stdin.readline

def solve():
    answer = []
    
    left_stack = list(input())
    right_stack = list()
    
    left_stack.pop()
    
    m = int(input())
    
    for _ in range(m):
        
        string = input()
        
        if len(string) == 2:
            cmd = list(string)
            
            if cmd[0] == 'L':
                if left_stack:
                    right_stack.append(left_stack.pop())
            
        
            if cmd[0] == 'D':
                if right_stack:
                    left_stack.append(right_stack.pop())
                    
            if cmd[0] == 'B':
                if left_stack:
                    left_stack.pop()
        
        else :
            cmd, char = string.split()
            left_stack.append(char)
            
    right_stack.reverse()
    left_stack.extend(right_stack)
    return left_stack

for i in solve():
    print(i,end='')