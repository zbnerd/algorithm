# 12865 평범한 배낭
import sys

input = sys.stdin.readline

n,k = map(int, input().split()) #n 물품의 수 k 버틸 수 있는 무게

weight = [0]
value = [0]

D = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1):
    w,v = map(int, input().split())
    
    for j in range(1,k+1):
        if j < w:
            D[i][j] = D[i-1][j]
        else :
            D[i][j] = max(D[i-1][j], D[i-1][j-w] + v)
            
print(max(D)[-1])