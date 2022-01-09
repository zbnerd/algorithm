#11403 경로 찾기
import sys
from copy import deepcopy
import random as r

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
n_list = []
            

for i in range(n):
    n_list.append(list(map(int,input().split())))

def test_print(arr):
    for c in arr:
        print(*c)
                
def floydWarshall(n_list):
    
    
    d = deepcopy((n_list))
    
    #k = 거쳐가는 노드
    for k in range(n):
        #i - 출발노드
        for i in range(n):
            #j - 도착노드
            for j in range(n):
                if d[i][j] == 1 or (d[i][k]== 1 and d[k][j] == 1):
                    d[i][j] = 1
    
    return d

test_print(floydWarshall(n_list))