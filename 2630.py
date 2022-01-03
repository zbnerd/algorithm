import sys
#2630 색종이 만들기
input = sys.stdin.readline

blue, white = 0,0
def divide(paper,n):
    
    global blue
    global white
    
    q1 = [row[n:] for row in paper[:n]]
    sigma1 = sum(x.count(1) for x in q1)
    if sigma1 == n**2:
        blue+=1
    elif sigma1 == 0:
        white+=1
    else:
        divide(q1,n//2)
        
        
    q2 = [row[:n] for row in paper[:n]] #2사분면
    sigma2 = sum(x.count(1) for x in q2)
    if sigma2 == n**2:
        blue+=1
    elif sigma2 == 0:
        white+=1
    else:
        divide(q2,n//2)
        
    q3 = [row[:n] for row in paper[n:]]
    sigma3 = sum(x.count(1) for x in q3)
    if sigma3 == n**2:
        blue+=1
    elif sigma3 == 0:
        white+=1
    else:
        divide(q3,n//2)
        
    q4 = [row[n:] for row in paper[n:]]
    sigma4 = sum(x.count(1) for x in q4)
    if sigma4 == n**2:
        blue+=1
    elif sigma4 == 0:
        white+=1
    else:
        divide(q4,n//2)
        

color_paper = []

n = int(input())

for _ in range(n):
    color_paper.append(list(map(int,input().split())))

sigma = sum(x.count(1) for x in color_paper)

if sigma == n**2:
    blue,white = 1,0
    
elif sigma == 0:
    blue,white = 0,1
    
else :
    divide(color_paper,n//2)

print(white)
print(blue)
