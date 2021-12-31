import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
#1922번 네트워크 연결

def find(x):
    if x == parent[x]:
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
    
def is_equall_parent(a,b):
    return find(a)==find(b)

n = int(input()) #컴퓨터의 수
parent_set = set()
m = int(input()) #연결할 수 있는 선의 수

graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input().split())
    #a 컴퓨터와 b컴퓨터를 연결하는데 비용이 c만큼 든다
    graph[c].append([a,b])
    
    parent_set.add(a)
    parent_set.add(b)
    
parent = [_ for _ in range(max(parent_set)+1)]

graph = sorted(graph.items())

spanning = []

for k in graph:
    for j in k[1]:
        if not is_equall_parent(j[0],j[1]):
            spanning.append(k[0])
            union(j[0],j[1])
        
print(sum(spanning))