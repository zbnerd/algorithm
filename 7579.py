import sys

input = sys.stdin.readline

n,m = map(int,input().split())
ai = [0]+list(map(int,input().split()))
ci = [0]+list(map(int,input().split()))

limit = sum(ci)

dp = [[0]*(limit+1) for i in range(n+1)]

for i in range(1,n+1):
    for w in range(1,len(dp[0])):
        if w < ci[i]:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-ci[i]]+ai[i])
            
for i in range(len(dp[n])):
    if dp[n][i] >= m:
        print(i)
        break