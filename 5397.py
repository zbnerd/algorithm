import sys

input = sys.stdin.readline

def solve():
    answer = []
    
    left_stack = list()
    right_stack = list()
    
    char = list(input())
    char.pop()
    
    for key in char:
        if key == '-':
            if left_stack:
                left_stack.pop()
        
        elif key == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        
        elif key == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        
        else :
            left_stack.append(key)
            
    right_stack.reverse()
    return left_stack+right_stack

T = int(input())

for T in range(T):
    print(''.join(solve()))