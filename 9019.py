import sys
from collections import deque
input = sys.stdin.readline

def L_generate(n):
    if n < 1000:
        n = n * 10
    
    else :
        thousand = n//1000
        n = (n % 1000) * 10 + thousand
        
    return n

def R_generate(n):
    one = n%10
    n //= 10
    n += (1000*one)
    
    return n

def solve():
    a,b = map(int,input().split())
    q = deque()
    visited = [False for _ in range(10001)]
    
    
    q.append((a,''))
    visited[a] = True
    

    while q:
        n, cmd = q.popleft()
        
        if n == b:
            print(cmd)
        
        D = (2*n)%10000
        if not visited[D]:
            visited[D] = True
            q.append((D,cmd+'D'))
        
        S = n-1
        if S == -1 :
            S = 9999
        if not visited[S]:
            visited[S] = True
            q.append((S,cmd+'S'))
        
        L = L_generate(n)
        if not visited[L]:
            visited[L] = True
            q.append((L,cmd+'L'))
            
        R = R_generate(n)
        if not visited[R]:
            visited[R] = True
            q.append((R,cmd+'R'))

        
    
    
for i in range(int(input())):
    solve()