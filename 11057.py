#11057 오르막수

import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(1001)]
ans = 0

#intialize
for i in range(10):
    dp[1][i] = 1

for i in range(1001):
    dp[i][0] = 1
    
#moduler
sum_moduler = lambda a,b : ((a%10007) + (b%10007)) % 10007

#generate dp table
for i in range(2,1001):
    for j in range(1,10):
        dp[i][j] = sum_moduler(dp[i-1][j],dp[i][j-1])
        
#add all dp[n] and substitude value to ans
for i in range(10):
    ans = sum_moduler(ans,dp[n][i])
    
print(ans)