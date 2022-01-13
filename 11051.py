import sys

input = sys.stdin.readline

def test_print(arr):
    for c in arr:
        print(*c)

n,k = map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if i == j or j == 0:
            dp[i][j] = 1
            
for i in range(1,n+1):
    for j in range(1,k+1):
        if i > j :
            dp[i][j] = dp[i-1][j]+dp[i-1][j-1]
            
print(dp[n][k])