import sys

input = sys.stdin.readline

def next_permutation(arr):
    i = len(arr)-1
    while arr[i-1] >= arr[i]:
        i -= 1
    
    if i == 0:
        return None
    
    for j in range(len(arr)-1,i-1,-1):
        if arr[j] > arr[i-1]:
            arr[i-1], arr[j] = arr[j], arr[i-1]
            break
    tmp = arr[i:]
    tmp.reverse()

    return arr[:i]+tmp

n = int(input())
cost = []

for i in range(n):
    cost.append(list(map(int,input().split())))
    
n_list = [i for i in range(n)]
total_cost = 9999999999

while n_list:

    tmp_cost = 0
    for i in range(n):
        if cost[n_list[i%n]][n_list[(i+1)%n]] == 0:
            tmp_cost = 9999999999
            break
        else :
            tmp_cost += cost[n_list[i%n]][n_list[(i+1)%n]]
    total_cost = min(total_cost, tmp_cost)
    
    n_list = next_permutation(n_list)


print(total_cost)