from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
world = [list(map(int, input().split())) for _ in range(N)]

#BFS를 이용한 국가번호 지정 및 다리 시작지점 추출 함수
def mark_nationNum_withBFS(coord):
    global nation_num

    q = deque()
    di, dj = [1,-1,0,0], [0,0,1,-1]

    q.append(coord)
    world[coord[0]][coord[1]] = nation_num

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if world[ni][nj] == 1:
                q.append((ni,nj))
                world[ni][nj] = nation_num

            elif world[ni][nj] == 0:
                bridge_startingPoint.add((ni, nj,nation_num))

    nation_num += 1

#BFS를 이용한 최소길이의 다리건설
def buildBridge_withBFS(starting_point):
    global bridge_lenList
    
    q = deque()
    si, sj = starting_point[0], starting_point[1]
    start_nation = starting_point[2]
    di, dj = [1,-1,0,0], [0,0,1,-1]

    terminated = False

    q.append((si, sj, start_bridgeLen))
    world[si][sj] = start_bridgeLen

    while q and not terminated:
        i, j, bridge_len = q.popleft()

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if not (0 <= ni < N and 0 <= nj < N):
                continue

            if world[ni][nj] == 0:
                world[ni][nj] = bridge_len+1
                q.append((ni, nj, bridge_len+1))

                
            elif world[ni][nj] != start_nation and 2 <= world[ni][nj] < nation_num:
                bridge_lenList.add(bridge_len-nation_num+1)
                terminated = True

#다리시작지점 추출
bridge_startingPoint = set()
nation_num = 2
for i in range(N):
    for j in range(N):
        if world[i][j] == 1:
            mark_nationNum_withBFS((i,j))

#다리건설
start_bridgeLen = nation_num
bridge_lenList = set()
for starting in bridge_startingPoint:
    buildBridge_withBFS(starting)

    for i in range(N):
        for j in range(N):
            if world[i][j] >= nation_num:
                world[i][j] = 0

#정답출력
print(min(bridge_lenList))