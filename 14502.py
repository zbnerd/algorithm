from itertools import combinations, chain
from copy import deepcopy
from collections import deque
import sys

input = sys.stdin.readline

def bfs(virus, lab):
    q = deque()
    for v in virus:
        q.append(v)
        lab[v[0]][v[1]] = 2

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if lab[ni][nj] == 0:
                    q.append((ni,nj))
                    lab[ni][nj] = 2

    return list(chain(*lab)).count(0)

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
di, dj = [1,-1,0,0], [0,0,1,-1]

wall = set()
virus = set()
new_wall = set()

for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == 0:
            new_wall.add((i,j))
        if lab[i][j] == 1:
            wall.add((i,j))
        if lab[i][j] == 2:
            virus.add((i,j))

safety_area = 0

for c in combinations(new_wall,3):
    new_lab = deepcopy(lab)

    new_lab[c[0][0]][c[0][1]] = 1
    new_lab[c[1][0]][c[1][1]] = 1
    new_lab[c[2][0]][c[2][1]] = 1

    safety_area = max(safety_area, bfs(virus, new_lab))

print(safety_area)