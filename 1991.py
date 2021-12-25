import sys

input = sys.stdin.readline

pre = []
in_ = []
post = []

def pre_order(idx):
    pre.append(binary_tree[idx])
    if binary_tree[idx*2] != '.':
        pre_order(idx*2)
    if binary_tree[idx*2+1] != '.':
        pre_order(idx*2+1)

def in_order(idx):
    if binary_tree[idx*2] != '.':
        in_order(idx*2)
    in_.append(binary_tree[idx])
    if binary_tree[idx*2+1] != '.':
        in_order(idx*2+1)
        
def post_order(idx):
    if binary_tree[idx*2] != '.':
        post_order(idx*2)
    if binary_tree[idx*2+1] != '.':
        post_order(idx*2+1)
    post.append(binary_tree[idx])
        
#루트 = 1
#왼쪽자식노드 = i*2
#오른쪽자식노드 = i*2+1

binary_tree = ['.']*100
binary_tree[1] = 'A'

for i in range(int(input())):
    parent, left, right = input().split()
    parent_idx = binary_tree.index(parent)
    binary_tree[parent_idx*2] = left
    binary_tree[parent_idx*2+1] = right
    
pre_order(1)
in_order(1)
post_order(1)

print(''.join(pre))
print(''.join(in_))
print(''.join(post))