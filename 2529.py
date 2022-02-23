k = int(input())
inequality_sign = input().split()
check = [False] * 10
ans_list = []

def g(x,y,op):
    if op == '<':
        if x > y: return False
    if op == '>':
        if x < y: return False

    return True

def recursion(i, num):
    
    if i == k+1:
        ans_list.append(num)
        return

    for j in range(10):
        if check[j] : continue
        if i == 0 or g(int(num[i-1]), j, inequality_sign[i-1]):
            check[j] = True
            recursion(i+1, num+str(j))
            check[j] = False
            
recursion(0, '')
print(ans_list[-1])
print(ans_list[0])