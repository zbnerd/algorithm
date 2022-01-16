#15990 1,2,3 더하기 5
import sys

input = sys.stdin.readline

dp = [0 for _ in range(100001)]
e1 = [0 for _ in range(100001)]
e2 = [0 for _ in range(100001)]
e3 = [0 for _ in range(100001)]

dp[1],dp[2],dp[3] = 1,1,3
e1[1],e2[1],e3[1] = 1,0,0
e1[2],e2[2],e3[2] = 0,1,0
e1[3],e2[3],e3[3] = 1,1,1

def sum_moduler(a,b):
    return ((a % 1000000009) + (b % 1000000009)) % 1000000009

def sub_moduler(a,b):
    return ((a % 1000000009) - (b % 1000000009) + 1000000009) % 1000000009

def dp_generate():
    global dp,e1,e2,e3
    
    for i in range(4,100001):
        d3 = sub_moduler(dp[i-3],e3[i-3])
        d2 = sub_moduler(dp[i-2],e2[i-2])
        d1 = sub_moduler(dp[i-1],e1[i-1])
        
        dp[i] = sum_moduler(sum_moduler(d3,d2),d1)
        
        e1[i] = d1
        e2[i] = d2
        e3[i] = d3
        
dp_generate()
for _ in range(int(input())):
    print(dp[int(input())])