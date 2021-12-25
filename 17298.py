import sys

input = sys.stdin.readline
#백준 17298 오큰수

n = int(input())
A = list(map(int,input().split()))
stack = []
nge = [-1]*len(A)

for i in range(len(A)):
    while stack and A[stack[-1]] < A[i]:
        nge[stack.pop()] = A[i]
        
    stack.append(i)

print(*nge)