import sys

input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return
    if x < y:
        parent[y] = x
    else :
        parent[x] = y

#n = 정점의 갯수, m = 간선의 갯수
n,m = map(int,input().split())


parent = [0]+[_ for _ in range(1,n+1)]
ans_set = set()

for _ in range(m):
    u,v = map(int,input().split())
    union(u,v)
    
for i in range(1,len(parent)):
    ans_set.add(parent[parent[i]])

print(len(list(ans_set)))