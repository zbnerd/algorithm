#1931 회의실 배정
import sys

input = sys.stdin.readline

conf_list = []
last, count = 0,0

for _ in range(int(input())):
    s,e =  map(int,input().split())
    conf_list.append([s,e])
    
conf_list.sort(key=lambda x: x[0])
conf_list.sort(key=lambda x: x[1])

for i,j in conf_list:
    if i >= last:
        count += 1
        last = j
        
print(conf_list)