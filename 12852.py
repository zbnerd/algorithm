import sys
from collections import deque

#백준 12852번 1로만들기 2

input = sys.stdin.readline

MAX = int(1e6)
MIN = 1

n = int(input())

parent = []
visit = []
q = deque()
visited = set()
visited.add(n)
res = []

q.append((n,0,0)) #숫자, 깊이, Flag
#Flag
# 3 = 3으로 나눔
# 2 = 2로 나눔
# 1 = 1을 뺌
# 0 = 루트


while q:
    val, depth, flag = q.popleft()
    if val == 1:
        break
    
    if val%3 == 0:
        if val//3 not in visited:
            q.append((val//3,depth+1,3))
            visit.append(val//3)
            parent.append(val)
            visited.add(val//3)
        
    if val%2 == 0:
        if val//2 not in visited:
            q.append((val//2,depth+1,2))
            visit.append(val//2)
            parent.append(val)
            visited.add(val//2)
        
    if val-1 not in visited:
        q.append((val-1,depth+1,1))
        visit.append(val-1)
        parent.append(val)
        visited.add(val-1)

res.append(1)

while n!=1:
    k = parent[visit.index(res[-1])]
    res.append(k)
    if k == n:
        break

res.reverse()
print(len(res)-1)
for r in res:
    print(r,end=' ')