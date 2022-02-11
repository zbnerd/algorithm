from collections import deque
from itertools import permutations
import sys

input = sys.stdin.readline

n = int(input())

def attack():
    q = deque()

    q.append((scv_hp[0],scv_hp[1],scv_hp[2],0))
    permut = list(permutations([9,3,1],3))
    visited = set()

    visited.add((scv_hp[0],scv_hp[1],scv_hp[2]))

    while q:
        a, b, c, atk_cnt = q.popleft()

        if a == 0 and b == 0 and c == 0:
            print(atk_cnt)
            break

        for d in permut:
            na, nb, nc, natk = a-d[0], b-d[1], c-d[2], atk_cnt+1
            if na < 0: na = 0
            if nb < 0: nb = 0
            if nc < 0: nc = 0

            if (na,nb,nc) not in visited:
                q.append((na,nb,nc,natk))
                visited.add((na,nb,nc))
        
scv_hp = [0,0,0]
scv_hp = list(map(int,input().split()))

if len(scv_hp) == 1: scv_hp += [0,0]
elif len(scv_hp) == 2: scv_hp += [0]

attack()