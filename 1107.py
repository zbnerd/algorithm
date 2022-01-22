from itertools import product
import sys

input = sys.stdin.readline

n = input()
m = int(input())

broken = set()

if m > 0:
    broken = set(map(int,input().split()))
    
keypad = set([0,1,2,3,4,5,6,7,8,9])-broken
product_list = []
push_cnt = 2147483647

for i in range(6):
    product_list.append(list(keypad))
    
    for c in product(*product_list):
        key_input = 0
        for i in range(len(c)):
            key_input += c[i]*pow(10,len(c)-i-1)
        
        pm_push_cnt = abs(int(n)-key_input)
        push_cnt = min(push_cnt,pm_push_cnt+len(product_list))
        
n_dif = abs(int(n)-100)
    
push_cnt = min(push_cnt,n_dif)
print(push_cnt)