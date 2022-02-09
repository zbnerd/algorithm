import sys

input = sys.stdin.readline
n = int(input())

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x == y: return

    if x < y: parent[y] = x
    else: parent[x] = y
        
        
planets = []

for i in range(n):
    x,y,z = map(int,input().split())
    planets.append([x,y,z,i])
    
graph = set()
for k in range(3):
    planets.sort(key = lambda x:x[k])
    for i in range(len(planets)-1):
        cost = min(abs(planets[i][0]-planets[i+1][0]), abs(planets[i][1]-planets[i+1][1]), abs(planets[i][2]-planets[i+1][2]))
        graph.add((cost, planets[i][3], planets[i+1][3]))
        graph.add((cost, planets[i+1][3], planets[i][3]))
        
parent = [i for i in range(n+1)]
mst = []
for c in sorted(graph):
    if find(c[1]) != find(c[2]):
        mst.append(c[0])
        union(c[1],c[2])

print(sum(mst))