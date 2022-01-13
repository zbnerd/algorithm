import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def chase_tree(istart,iend,pstart,pend):
    if istart > iend or pstart > pend :
        return
    
    node = post_order[pend]
    print(node,end=' ')
    offset = in_order_pos[node]
    
    left = offset-istart #왼쪽 트리 자식 갯수
    right = iend-offset #오른쪽 트리 자식 갯수
    
    #left range = start ~ (start+left-1)
    chase_tree(istart,istart+left-1,pstart,pstart+left-1)
    
    #right range
    #in_order end-right+1 ~ end
    #post_order end-right ~ end-1
    chase_tree(iend-right+1,iend,pend-right,pend-1)
    
n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))
in_order_pos = [0]*(n+1)

for i in range(len(in_order)):
    in_order_pos[in_order[i]] = i

chase_tree(0,n-1,0,n-1)