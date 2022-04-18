import sys
from collections import deque

input = sys.stdin.readline

def bfs(s,e):
    q = deque()
    q.append((s,0))
    
    
    

    visited[s] = True
        
    while q:
        p, c = q.popleft()

        if p == e:
            print(c)
            return
                
        #일의 자리 바꾸기
        one_digit = p-(p%10)
        for i in range(one_digit, one_digit+10):
            if not visited[i] and is_prime[i]:
                visited[i] = True
                q.append((i,c+1))
        
        #십의 자리 바꾸기
        ten_digit = p-(p%100//10*10)
        for i in range(ten_digit, ten_digit+99,10):
            if not visited[i] and is_prime[i]:
                visited[i] = True
                q.append((i,c+1))
        
        #백의 자리 바꾸기
        hundred_digit = p-(p%1000//100*100)
        for i in range(hundred_digit, hundred_digit+999,100):
            if not visited[i] and is_prime[i]:
                visited[i] = True
                q.append((i,c+1))
        
        #천의 자리 바꾸기
        thousand_digit = p-(p%10000//1000*1000)+1000
        for i in range(thousand_digit, 10000, 1000):
            if not visited[i] and is_prime[i]:
                visited[i] = True
                q.append((i,c+1))
        
    print('Impossible')
        


    
t = int(input())

n = [i for i in range(10000)]
is_prime = [False] * 10000
visited = [False] * 10000

n[1] = 0

for i in range(2,101):
    for j in range(2*i,10000,i):
        n[j] = 0
        
for i in range(10000):
    is_prime[i] = (n[i] != 0)
    
for i in range(1000):
    visited[i] = True
    
for _ in range(t):
    s,e = map(int,input().split())
    bfs(s,e)
    for i in range(10000):
        visited[i] = False