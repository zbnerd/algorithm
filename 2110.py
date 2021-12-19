import sys

input = sys.stdin.readline

n,c = map(int,input().split())
house_coord = []

for i in range(n):
    house_coord.append(int(input()))
    
house_coord.sort()

min_dist = 1
max_dist = house_coord[-1]
routers = 1

while min_dist <= max_dist:
    mid = (min_dist+max_dist) // 2
    
    routers = 1
    
    pivot = house_coord[0]
    for i in range(1,len(house_coord)):
        if house_coord[i]-pivot >= mid:
            routers+=1
            pivot = house_coord[i]
            
    if routers < c :
        max_dist = mid-1
    else :
        min_dist = mid+1
        
print(max_dist)