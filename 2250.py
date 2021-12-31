import sys
from collections import defaultdict
import copy

input = sys.stdin.readline

#2250번 트리의 높이와 너비

#중위순회 순서 번호를 지정해주기위한 변수
cnt = 1
# 중위 순회
def inorder(n):
    
    global cnt
    
    if Nodes[n]['left'] != -1:
        Nodes[Nodes[n]['left']]['level'] = Nodes[n]['level']+1
        inorder(Nodes[n]['left'])
    Nodes[n]['order'] = cnt
    cnt += 1
    if Nodes[n]['right'] != -1:
        Nodes[Nodes[n]['right']]['level'] = Nodes[n]['level']+1
        inorder(Nodes[n]['right'])
    
#노드 갯수
n = int(input())

#이진트리 노드 저장할 딕셔너리
Nodes = dict()

#모든 저장된 노드들을 담아두는 set
num_set = set()

#자식들만 담아두는 set
child_set = set()

#루트노드는 아무거나 우선 초기화해둔다.
root_node = 1

#이진트리 정보 입력
for i in range(n):
    #노드 번호, 왼쪽자식, 오른쪽자식
    num, left, right = map(int,input().split())
    node = dict()
    node['left'] = left
    node['right'] = right
    node['order'] = -1 #중위순회하는데 순서 번호를 저장하기 위함. 즉 order번호가 열번호가 된다.
    node['level'] = -1 #레벨은 행 번호가 된다.
    
    num_set.add(num) #모든 노드들을 담아둔다.
    child_set.add(left) #자식노드만 담아둔다.
    child_set.add(right) #자식노드만 담아둔다.
    
    Nodes[num] = node

#자식노드에 없는 번호가 딱 하나 발견되는데 이게 바로 루트노드.
for i in num_set:
    if i not in child_set:
        root_node = i
        
#루트노드 레벨값 설정      
Nodes[root_node]['level'] = 1

#중위순회 - 여기서 행번호(레벨)와 열번호(중위순회 순서값)가 정해진다.
inorder(root_node)


levels = defaultdict(list)
lev_width = []

#모든 노드들을 순회하면서 레벨별로 열 번호를 리스트로 담는다.
for k,v in Nodes.items():
    levels[Nodes[k]['level']].append(Nodes[k]['order'])

#노드 레벨별로 너비값을 구해준다.
for k,v in levels.items():
    minimum = min(v)
    maximum = max(v)
    lev_width.append([maximum-minimum+1,k])

#최우선적으로 너비값을 내림차순으로, 그다음 레벨값을 오름차순으로 정렬한다.
sorted_width = sorted(lev_width, key = lambda x : (-x[0],x[1]))

#값 출력한다.
print(sorted_width[0][1],sorted_width[0][0])
   
