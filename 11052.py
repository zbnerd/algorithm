#11052 카드 구매하기
import sys

input = sys.stdin.readline

n = int(input())
p = [0]+list(map(int, input().split()))

DP = [p[i] for i in range(n+1)]

for i in range(2,n+1):
    for j in range(1,i):
        DP[i] = max(DP[i],p[i-j]+DP[j])
        
print(DP[n])