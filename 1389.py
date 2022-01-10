import sys

input = sys.stdin.readline

INF = sys.maxsize

n,m = map(int,input().split())

adj_matrix = [[INF]*(n) for _ in range(n)]
bacon_list = []

for i in range(n):
    adj_matrix[i][i] = 0

for _ in range(m):
    a,b = map(int,input().split())
    
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1


for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] > (adj_matrix[i][k]+adj_matrix[k][j]):
                adj_matrix[i][j] = adj_matrix[i][k]+adj_matrix[k][j]

for i in range(n):
    for j in range(n):
        if adj_matrix[i][j] == INF :
            adj_matrix[i][j] = 0
            

for i in range(n):
    bacon = 0
    for j in range(n):
        if adj_matrix[i][j] != INF :
            bacon += adj_matrix[i][j]
    
    bacon_list.append(bacon)
    
min_bacon = min(bacon_list)
print(bacon_list.index(min_bacon)+1)