#23061 백남이의 여행 준비 #시간초과
import sys

input = sys.stdin.readline

#n - 물품의 수
#m = 가방의 수
n,m = map(int,input().split())

w = [0]
v = [0]

D = []

max_effi_bag = -1
max_effi = -1

for i in range(n):
    wi, vi = map(int,input().split())
    w.append(wi)
    v.append(vi)
    
for i in range(m):
    limit = int(input())
    D = [[0]*(limit+1) for _ in range(n+1)]
    
    for a in range(1,n+1):
        for b in range(1,limit+1):
            if b < w[a]:
                D[a][b] = D[a-1][b]
            else:
                D[a][b] = max(D[a-1][b], D[a-1][b-w[a]]+v[a])
    
    if D[n][limit]/limit > max_effi:
        max_effi = D[n][limit]/limit
        max_effi_bag = i+1
        

print(max_effi_bag)
    
