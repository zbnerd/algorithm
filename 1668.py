import sys

input = sys.stdin.readline

trophy_height = [int(input()) for _ in range(int(input()))]
left_c = 1
right_c = 1

left_trophy_max_height = trophy_height[0]
right_trophy_max_height = trophy_height[-1]

for i in range(1,len(trophy_height)):
    if left_trophy_max_height < trophy_height[i]:
        left_trophy_max_height = trophy_height[i]
        left_c += 1
        
for i in range(2,len(trophy_height)+1):
    if right_trophy_max_height < trophy_height[-i]:
        right_trophy_max_height = trophy_height[-i]
        right_c += 1
        
print(left_c)
print(right_c)