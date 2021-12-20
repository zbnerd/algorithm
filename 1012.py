import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline


def flood_fill(x,y):
    if farm[x][y] == 0:
        return
    
    farm[x][y] = 0
    if y<(len(farm[0])-1):
        flood_fill(x,y+1)
    
    if x<(len(farm)-1):
        flood_fill(x+1,y)
    
    if x>0:
        flood_fill(x-1,y)
    
    if y>0:
        flood_fill(x,y-1)
    
t = int(input())
for i in range(t):
    farm = []
    warm_cnt = 0
    m,n,k = map(int,input().split())
    
    for i in range(n):
        farm.append([0]*m)
        
    for i in range(k):
        a,b = map(int,input().split())
        farm[b][a] = 1

    for i in range(len(farm)):
        for j in range(len(farm[i])):
            if farm[i][j] == 1:
                warm_cnt+=1
                flood_fill(i,j)

    print(warm_cnt)