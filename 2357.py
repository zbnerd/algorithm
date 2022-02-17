import sys

input = sys.stdin.readline

n,m = map(int,input().split())
INF = float('inf')

n_list = [int(input()) for i in range(n)]

min_tree = [0]*(n*4)
max_tree = [0]*(n*4)

def min_init(start, end, node):
    if start == end:
        min_tree[node] = n_list[start]
        return min_tree[node]
    
    mid = (start + end) // 2
    min_tree[node] = min(min_init(start, mid, node * 2), min_init(mid+1, end, node * 2 + 1))

    return min_tree[node]

def max_init(start, end, node):
    if start == end:
        max_tree[node] = n_list[start]
        return max_tree[node]
    
    mid = (start + end) // 2
    max_tree[node] = max(max_init(start, mid, node * 2), max_init(mid+1, end, node * 2 + 1))

    return max_tree[node]

def minimum(start, end, node, left, right):
    #out of range
    if left > end or right < start :
        return INF
    
    #in of range
    if left <= start and end <= right:
        return min_tree[node]

    mid = (start+end) // 2

    return min(minimum(start, mid, node * 2, left, right), minimum(mid+1, end, node * 2 + 1, left, right))

def maximum(start, end, node, left, right):
    #out of range
    if left > end or right < start :
        return 0
    
    #in of range
    if left <= start and end <= right:
        return max_tree[node]

    mid = (start+end) // 2

    return max(maximum(start, mid, node * 2, left, right), maximum(mid+1, end, node * 2 + 1, left, right))

min_init(0, n-1, 1)
max_init(0, n-1, 1)

for _ in range(m):
    a, b = map(int,input().split())

    if a > b:
        a, b = b, a

    print(minimum(0, n-1, 1, a-1, b-1), maximum(0, n-1, 1, a-1, b-1))