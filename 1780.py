#1780 종이의 개수
import sys
sys.setrecursionlimit(2**18)

input = sys.stdin.readline



paper1,paper0,paperM1 = 0,0,0

def test_print(arr):
    for c in arr:
        print(*c)

def divide(paper,n):
    global paperM1,paper0,paper1
    countM1 = sum(x.count(-1) for x in paper)
    count1 = sum(x.count(1) for x in paper)
    count0 = sum(x.count(0) for x in paper)
    
    if countM1 == n**2:
        paperM1 += 1
    
    elif count1 == n**2:
        paper1 += 1
        
    elif count0 == n**2:
        paper0 += 1
        
    else :
        divide([x[:n//3] for x in paper[:n//3]],n//3)
        divide([x[n//3:n-n//3] for x in paper[:n//3]],n//3)
        divide([x[n-n//3:] for x in paper[:n//3]],n//3)
        divide([x[:n//3] for x in paper[n//3:n-n//3]],n//3)
        divide([x[n//3:n-n//3] for x in paper[n//3:n-n//3]],n//3)
        divide([x[n-n//3:] for x in paper[n//3:n-n//3]],n//3)
        divide([x[:n//3] for x in paper[n-n//3:]],n//3)
        divide([x[n//3:n-n//3] for x in paper[n-n//3:]],n//3)
        divide([x[n-n//3:] for x in paper[n-n//3:]],n//3)
        
n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, input().split())))

divide(paper,n)
print(paperM1)
print(paper0)
print(paper1)
