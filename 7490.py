import sys
import copy

input = sys.stdin.readline

operators = []

def recursive(array,n):
    if len(array) == n:
        
        operators.append(copy.deepcopy(array))
        return
    
    array.append(' ')
    recursive(array,n)
    array.pop()
    
    array.append('+')
    recursive(array,n)
    array.pop()
    
    array.append('-')
    recursive(array,n)
    array.pop()

def solve():
    n = int(input())
    recursive([],n-1)
    n_list = [a for a in range(1,n+1)]
    
    
    for i in operators:
        string = str(n_list[0])
        for j in range(len(i)):
            string += (i[j] + str(n_list[j+1]))
        operations = eval(string.replace(' ',''))
        if operations == 0:
            print(string)
    print()

for _ in range(int(input())):
    operators.clear()
    solve()
