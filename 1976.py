import sys

input = sys.stdin.readline
#1976번 여행가자

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x,y):
    x = find(x)
    y = find(y)
    
    if x<y:
        parent[y] = x
    else :
        parent[x] = y
    
#n = 도시의 수
n = int(input())
adjacent_matrix = []
parent = [_ for _ in range(n+1)]

#m = 여행 계획에 속한 도시들의 수
m = int(input())

#인접행렬
adjacent_matrix.append([0]*(n+1))
for _ in range(n):
    adjacent_matrix.append([0]+list(map(int,input().split())))

#인접행렬 원소가 1이면 i,j번째 도시는 연결된것
for i in range(1,len(adjacent_matrix)):
    for j in range(1,len(adjacent_matrix[i])):
        if adjacent_matrix[i][j] == 1:
            union(i,j)

#도시 여행 계획
m_list = list(map(int, input().split()))

possible = True

#도시가 연결되어있으면 여행이 가능. 즉 해당 도시번호의 루트노드가 같으면 Yes 하나라도 연결이 되어있지않는경우는 No
for i in range(1,len(m_list)):
    if find(parent[m_list[i-1]]) != find(parent[m_list[i]]):
        possible = False
        break
        

    
print('YES' if possible else 'NO')