#1495 기타리스트
import sys
from collections import deque

def test_print(arr):
    for c in arr:
        print(*c)

#n 곡의 갯수, s 시작볼륨, m 최대볼륨
n,s,m = map(int,input().split())
v = list(map(int,input().split()))
D = []

for i in range(n):
    D.append([0]*(m+1))

p = s+v[0]

if p <= m:
    D[0][p] = 1
    
p = s-v[0]

if p >= 0:
    D[0][p] = 1

for i in range(1,len(D)):
    for j in range(len(D[i-1])):
        if D[i-1][j] == 1:
            p = j+v[i]
            if p <= m:
                D[i][p] = 1
            p = j-v[i]
            if p >= 0:
                D[i][p] = 1

if D[len(D)-1].count(1) == 0:
    print(-1)
else :
    ans = 0
    for i in range(len(D[len(D)-1])):
        if D[len(D)-1][i] == 1:
            ans = i

    print(ans)
            