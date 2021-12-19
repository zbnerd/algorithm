import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def get_parent(x):
    if parent[x] != x:
        parent[x] = get_parent(parent[x])

    return parent[x]

def union_node(a, b):
    a = get_parent(a)
    b = get_parent(b)
    
    if a!=b:
        parent[b] = a
        
def is_equall_rootnode(a,b):
    return get_parent(a) == get_parent(b)
    

n = int(input())
m = int(input())
ans = 0

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    a,b = map(int,input().split())
    union_node(a,b)
    
for i in range(2,n+1):
    if is_equall_rootnode(1,i):
        ans+=1

print(ans)