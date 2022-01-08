import sys
from bisect import bisect_left

#2568 전깃줄 2

input = sys.stdin.readline

n = int(input())
utility_pole = []
util_set = set()

for _ in range(n):
    a,b = map(int,input().split())
    utility_pole.append((a,b))
    util_set.add(a)
    
utility_pole.sort()

L = [1]
D = [utility_pole[0][1]]
LIS = []


for i in range(1,len(utility_pole)):
    if D[-1] < utility_pole[i][1]:
        D.append(utility_pole[i][1])
        L.append(len(D))
    
    else:
        bi = bisect_left(D,utility_pole[i][1])
        L.append(bi+1)
        D[bi] = utility_pole[i][1]
        
maxL = max(L)

print(n-maxL)

for i in range(n-1,-1,-1):
    if L[i] == maxL:
        LIS.append(utility_pole[i][0])
        maxL-=1
    
for c in sorted(util_set-set(LIS)):
    print(c)