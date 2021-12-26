import sys

input = sys.stdin.readline
#11728 배열 합치기

n,m = map(int,input().split())
i,j = 0,0

n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))

res = n_list+m_list
        
print(*sorted(res))