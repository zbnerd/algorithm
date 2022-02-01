from collections import defaultdict
import heapq, sys

input = sys.stdin.readline

def dijkstra(start):
    distance = [float('inf')] * (v+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        
        if distance[node] < dist:
            continue
        
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

    return distance

def get_longest_vertex(v):
    longest_dist = 0
    longest_v = -1
    dist_table = dijkstra(v)

    for i in range(1,len(dist_table)):
        if longest_dist < dist_table[i]:
            longest_dist = dist_table[i]
            longest_v = i

    return longest_v, longest_dist

v = int(input())
graph = defaultdict(list)

for i in range(v):
    input_list = list(map(int, input().split()))
    for j in range(1,len(input_list)-1,2):
        graph[input_list[0]].append((input_list[j],input_list[j+1]))
        
print(get_longest_vertex(get_longest_vertex(1)[0])[1])