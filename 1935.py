import sys

input = sys.stdin.readline
#백준 1935번 후위표기식 2

#피연산자 갯수
n = int(input())

#미지수를 딕셔너리로 저장
unknown_quantity = dict()

#후위표기식
post_fix = input()

#후위표기식 값 처리를 위한 스택
stack = []

#미지수 값을 딕셔너리에 저장
for i in range(n):
    unknown_quantity[chr(i+65)] = int(input())
    
for i in range(len(post_fix)):
    
    #연산자 - 피연산자 두개를 꺼내고 계산 후 다시 스택에 push
    
    if i != len(post_fix) -1:
        a,b = 0,0
        if post_fix[i] == '+':
            a,b = stack.pop(),stack.pop()
            stack.append(b+a)
        elif post_fix[i] == '-':
            a,b = stack.pop(),stack.pop()
            stack.append(b-a)
        elif post_fix[i] == '*':
            a,b = stack.pop(),stack.pop()
            stack.append(b*a)
        elif post_fix[i] == '/':
            a,b = stack.pop(),stack.pop()
            stack.append(round(b/a,2))

        #피연산자 - 스택에 삽입
        else :
            stack.append(unknown_quantity[post_fix[i]])
    else :
        print("%.2f"%stack.pop())