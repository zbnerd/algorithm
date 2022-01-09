#1992 쿼드 트리
import sys

input = sys.stdin.readline

quad_tree = []
def test_print(arr):
    for c in arr:
        print(*c)

#재귀
def divide(matrix,n):
    element_sigma = sum(sum(x) for x in matrix)
    
    if element_sigma == 0:
        quad_tree.append('0')
    elif element_sigma == n**2:
        quad_tree.append('1')
    else:
        quad_tree.append('(')
        divide([row[:n//2] for row in matrix[:n//2]],n//2)
        divide([row[n//2:] for row in matrix[:n//2]],n//2)
        divide([row[:n//2] for row in matrix[n//2:]],n//2)
        divide([row[n//2:] for row in matrix[n//2:]],n//2)
        quad_tree.append(')')
    
    

n = int(input())
matrix = []

#쿼드트리 입력
for i in range(n):
    matrix.append(list(map(int,list(input()[:-1]))))
    
divide(matrix,n)
print(''.join(quad_tree))