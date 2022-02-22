from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int,input().split())) for _ in range(n)]
ans = float('inf')

def team(i, first, second):
    global ans

    if i == n+1:
        return

    if len(first) > n//2 :
        return
    
    if len(second) > n//2 :
        return

    if len(first) == n//2 and len(second) == n//2:
        t1 = 0
        t2 = 0
        for t in combinations(first,2):
            t1 += s[t[0]][t[1]]
            t1 += s[t[1]][t[0]]

        for t in combinations(second,2):
            t2 += s[t[0]][t[1]]
            t2 += s[t[1]][t[0]]

        diff = abs(t1-t2)
        ans = min(ans, diff)


    team(i+1, first+[i], second)
    team(i+1, first, second+[i])
    
team(0,[],[])
print(ans)