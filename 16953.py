#16953 A → B
import sys
from collections import deque

input = sys.stdin.readline

a,b = map(int,input().split())
q = deque()

q.append((a,0))
visited = set()
visited.add(a)
res = -1

while q:
    pop, count = q.popleft()
    
    if pop == b:
        res = count+1
        break
    
    x2 = pop*2
    if x2 not in visited:
        if x2 <= b:
            visited.add(x2)
            q.append((x2,count+1))
        
    append1 = pop*10+1
    if append1 not in visited:
        if append1 <= b:
            visited.add(append1)
            q.append((append1,count+1))
        
print(res)