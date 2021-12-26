import sys

input = sys.stdin.readline
#4195번 친구 네트워크

parent = dict()
connected = dict()


#유니온 파인드 함수
def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x,y):
    unions = [find(x),find(y)]
    unions.sort()
    
    if unions[0] != unions[1]:
        parent[unions[1]] = unions[0]
        connected[unions[0]] += connected[unions[1]]
    
    
def solve():
    #친구 관계의 수만큼 입력
    for _ in range(int(input())):
        p1, p2 = input().split()
        
        if p1 not in parent:
            parent[p1] = p1
            connected[p1] = 1
        if p2 not in parent:
            parent[p2] = p2
            connected[p2] = 1
        
        union(p1,p2)
        print(connected[find(p1)])
        
            
for _ in range(int(input())):
    solve()
    parent.clear()
    connected.clear()
    
