import sys
from collections import Counter

input = sys.stdin.readline
#백준 17298 오등큰수

n = int(input())
A = list(map(int,input().split()))
F = Counter(A)
stack = []
ngf = [-1]*len(A)

for i in range(len(A)):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        ngf[stack.pop()] = A[i]
        
    stack.append(i)

print(*ngf)