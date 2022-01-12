import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def chase_tree(istart,iend,pstart,pend):
    if istart > iend or pstart > pend:
        return
    
    print(post_order_list[pend],' ')
    inorder_offset = in_order_list.index(post_order_list[pend])
    
    
    #left child
    chase_tree(istart,inorder_offset-1,pstart,inorder_offset-1)
    #right child
    chase_tree(inorder_offset+1,iend,inorder_offset,pend-1)
    

n = int(input())
in_order_list = list(map(int,input().split()))
post_order_list = list(map(int,input().split()))

chase_tree(0,n-1,0,n-1)