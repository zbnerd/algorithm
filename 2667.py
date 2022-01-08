#2667 단지번호 붙이기
import sys
sys.setrecursionlimit(2**18)

input = sys.stdin.readline
complex_count = 0
visited = 1

complex_count_list = list()

def flood_fill(x,y):
    global complex_count
    
    house_complex[x][y] = visited
    complex_count += 1
    
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        if not((nx == -1 or ny == -1) and (nx == n or ny == n)):
            if house_complex[nx][ny]==1:
                flood_fill(nx,ny)
    
    

def test_print(arr):
    for c in arr:
        print(*c)

n = int(input())
house_complex = [[0]*(n+2)]

dx,dy = [0,0,1,-1],[1,-1,0,0]

for _ in range(n):
    house_complex.append([0]+list(map(int,input()[:-1]))+[0])
    
house_complex.append([0]*(n+2))
    
for i in range(len(house_complex)):
    for j in range(len(house_complex[i])):
        if house_complex[i][j] == 1:
            visited+=1
            flood_fill(i,j)
            
for i in range(2,visited+1):
    complex_count_list.append((sum(x.count(i) for x in house_complex)))
    
complex_count_list.sort()
print(len(complex_count_list))
for i in range(len(complex_count_list)):
    print(complex_count_list[i])
            