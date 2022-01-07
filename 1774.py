#1774 우주신과의 교감
import sys
from collections import defaultdict

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

def find(x):
    if x == parent[x]:
        return x
    else :
        parent[x] = find(parent[x])
        return parent[x]

def union(u,v):
    u = find(u)
    v = find(v)
    
    if u==v:
        return
    
    if u < v:
        parent[v] = u
    else :
        parent[u] = v

input = sys.stdin.readline

n,m = map(int,input().split())

mst = []
graph = []
parent = [i for i in range(n+1)]

coord = []

#우주신들 연결
for i in range(1,n+1):
    x,y = map(int,input().split())
    #x,y,우주신번호
    coord.append((x,y,i))
    
for i in range(len(coord)):
    for j in range(i+1,len(coord)):
        x1,y1 = coord[i][0],coord[i][1]
        x2,y2 = coord[j][0],coord[j][1]
        a = coord[i][2]
        b = coord[j][2]
        graph.append([distance(x1,y1,x2,y2),a,b])
        graph.append([distance(x1,y1,x2,y2),b,a])
    
for i in range(m):
    x,y = map(int,input().split())
    union(x,y)
    
graph_list = sorted(list(graph))
sum_len = 0.00

for length,a,b in graph_list:
    if find(a) != find(b):
        sum_len += length
        union(a,b)
        
print("{:.2f}".format(sum_len))