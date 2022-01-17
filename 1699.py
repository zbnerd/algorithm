import sys

input = sys.stdin.readline

n = int(input())

squares = []
dp = [float('inf')] * 100001
for i in range(1,317):
    dp[i*i] = 1
    
for i in range(1,317):
    squares.append(i*i)
    
for i in range(2,100001):
    for s in squares:
        j = i-s
        if j < 1:
            break
        dp[i] = min(dp[i],dp[j]+1)
        
print(dp[n])