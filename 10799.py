import sys

input = sys.stdin.readline

string = list(input())
string.pop()
answer = 0
stack = []

for i in range(len(string)) :
    if string[i] == '(':
        stack.append(string[i])
    else :
        if i > 0:
            if string[i-1] == '(':
                stack.pop()
                answer += len(stack)

            else :
                stack.pop()
                answer += 1
            
print(answer)