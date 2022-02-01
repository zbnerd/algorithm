from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

n_list = [-1] * n

a_idx = [-1] * n

LIS_length = [1] * len(n_list)
max_len = 0

for i, e in enumerate(a):
    a_idx[e-1] = i

for i in range(n):
    n_list[i] = a_idx[b[i]-1]

LIS = [n_list[0]]

for i in range(1,len(n_list)):
    if LIS[-1] < n_list[i]:
        LIS.append(n_list[i])
        LIS_length[i] = len(LIS)
        max_len = LIS_length[i]

    else:
        LIS_length[i] = bisect_left(LIS,n_list[i])
        LIS[LIS_length[i]] = n_list[i]

ans = []

l = 1
for i in range(len(LIS_length)):
    if LIS_length[i] == l:
        ans.append(n_list[i])
        l += 1

print(len(ans))