import sys

input = sys.stdin.readline

n = int(input())
sec = 0
k = 1

while n>0:
    n-=k
    if k>=n:
        k=1
    else:
        k+=1
    sec += 1
    
print(sec)