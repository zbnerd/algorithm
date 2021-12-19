import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_node(a, b):
    a = get_parent(a)
    b = get_parent(b)
    
    if a<b:
        parent[b] = a
    else :
        parent[a] = b
        
def is_equall_rootnode(a,b):
    return get_parent(a) == get_parent(b)
    

n,m = map(int,input().split())

parent = [_ for _ in range(n+1)]

for i in range(m):
    c,a,b = map(int,input().split())
        
    if c==0: #union
        union_node(a,b)
    else :
        print('yes' if is_equall_rootnode(a,b) else 'no')