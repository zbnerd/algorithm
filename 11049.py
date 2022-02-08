import sys

input = sys.stdin.readline

n = int(input())
d = []
dp = [[-1]*(n+1) for i in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

for i in range(n):
    a, b = map(int,input().split())
    if i == 0:
        d.append(a)
    d.append(b)
    
for diagnal in range(1,n):
    ei = n-diagnal+1
    for i in range(1,ei):
        j = i+diagnal
        tmp = []
        for k in range(i,j):
            value = dp[i][k]+dp[k+1][j]
            value += d[i-1]*d[k]*d[j]
            tmp.append(value)
        dp[i][j] = min(tmp)
        
print(dp[1][n])