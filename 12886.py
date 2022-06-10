from collections import deque
import sys

input = sys.stdin.readline

a,b,c = map(int, input().split())

def bfs(a,b,c):
    q = deque()

    visited = set()

    q.append([a,b,c])
    visited.add((a,b,c))

    while q:
        pop = q.popleft()

        if pop[0] == pop[1] and pop[1] == pop[2]:
            return 1

        #1,2번째
        pop_copy1 = pop[:]
        flag = -1

        if pop_copy1[0] > pop_copy1[1]:
            flag = 0

        elif pop_copy1[0] < pop_copy1[1]:
            flag = 1

        else :
            flag = 2

        if flag == 0:
            pop_copy1[0] -= pop_copy1[1]
            pop_copy1[1] *= 2

        elif flag == 1:
            pop_copy1[1] -= pop_copy1[0]
            pop_copy1[0] *= 2

        if tuple(pop_copy1) not in visited:
            visited.add(tuple(pop_copy1))
            q.append(pop_copy1)

        #2,3번째
        pop_copy2 = pop[:]
        flag = -1

        if pop_copy2[1] > pop_copy2[2]:
            flag = 0

        elif pop_copy2[1] < pop_copy2[2]:
            flag = 1

        else :
            flag = 2

        if flag == 0:
            pop_copy2[1] -= pop_copy2[2]
            pop_copy2[2] *= 2            

        elif flag == 1:
            pop_copy2[2] -= pop_copy2[1]
            pop_copy2[1] *= 2

        if tuple(pop_copy2) not in visited:
            visited.add(tuple(pop_copy2))
            q.append(pop_copy2)

        #1,3번째
        pop_copy3 = pop[:]
        flag = -1

        if pop_copy3[0] > pop_copy3[2]:
            flag = 0

        elif pop_copy3[0] < pop_copy3[2]:
            flag = 1

        else :
            flag = 2

        if flag == 0:
            pop_copy3[0] -= pop_copy3[2]
            pop_copy3[2] *= 2            

        elif flag == 1:
            pop_copy3[2] -= pop_copy3[0]
            pop_copy3[0] *= 2

        if tuple(pop_copy3) not in visited:
            visited.add(tuple(pop_copy3))
            q.append(pop_copy3)

    return 0

print(bfs(a,b,c))