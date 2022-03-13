from collections import defaultdict, deque
import sys

input = sys.stdin.readline

# 올바른 순서대로 자식들이 배열되었는가 판별하는 함수
def is_vaild_order():
    q2 = deque()
    q2.append(1)
    start = 1

    while q2:
        pop = q2.popleft()
        
        a = set(childs[pop])

        len_a = len(a)
        b = visit_order[start:start+len_a]
        q2.extend(b)
        b = set(b)

        start += len_a

        if a != b:
            return False

    return True

# 올바른 깊이대로 배열되었는가 판별하는 함수
def is_vaild_level():

    start = 0
    for level, value in depth.items():
        if set(visit_order[start:start+len(value)]) != set(value):
            return False
        start += len(value)

    return True

def bfs():
    q = deque()
    visited = set()

    q.append((1,1))
    visited.add(1)

    while q:
        vertex, level = q.popleft()

        depth[level].append(vertex)

        for adj in graph[vertex]:
            if adj not in visited:
                q.append((adj,level+1))
                visited.add(adj)
                childs[vertex].append(adj)

# 입력
n = int(input())
depth = defaultdict(list) # 트리의 깊이를 저장
graph = defaultdict(list) # 그래프 저장
childs = defaultdict(list) # 각 원소마다의 자식들을 저장

# 그래프 입력
for _ in range(n-1):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)
    
# 트리의 깊이와 자식들을 저장해주기위해 너비우선탐색 실행
bfs()

# 트리 순회 순서 입력
visit_order = list(map(int, input().split()))
print(1 if is_vaild_level() and is_vaild_order() else 0)