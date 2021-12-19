import sys

input = sys.stdin.readline

#세로크기 n 가로크기 m
n,m = map(int,input().split())

castle = []
row = [0]*n
col = [0]*m

for i in range(n):
    s = list(input())
    s.pop()
    castle.append(s)

for i in range(len(castle)):
    for j in range(len(castle[i])):
        if castle[i][j] == 'X':
            row[i] = 1
            col[j] = 1
            
print(max(row.count(0),col.count(0)))