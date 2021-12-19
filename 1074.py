import sys

input = sys.stdin.readline

c_list = [0,1,4,5] #n=2
r_list = [] #n=2

def solve(n):
    for k in range(3,n+1):
        for i in range(len(c_list)):
            c_list.append(c_list[i]+2**(2*k-2))
            
    for c in c_list:
        r_list.append(c*2)
        
n,r,c = map(int, input().split())
solve(n)

print(r_list[r]+c_list[c])