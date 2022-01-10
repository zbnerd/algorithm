#9375 패션왕 신해빈
from collections import defaultdict

def solve():
    ans = 1
    
    n = int(input())
    clothes = defaultdict(list)
    comb_list = []
    
    for i in range(n):
        a,b = input().split()
        clothes[b].append(a)
    
    for v in clothes.values():
        ans *= (len(v)+1)
        
    print(ans-1)
    
for _ in range(int(input())):
    solve()