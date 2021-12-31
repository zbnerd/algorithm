import sys
import heapq

input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    n = int(input())
    if n:
        heapq.heappush(heap,n)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)