# 11053 가장 긴 증가하는 부분 수열
import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
L = [1]*n

for i in range(1,n):
    for j in range(i):
        if A[j] < A[i]:
            L[i] = max(L[i],L[j]+1)
            
print(max(L))