def solve(m,n,x,y):
    k = x
    while k <= m*n:
        if (k-y)%n == 0:
            return k
        k += m
    return -1

for _ in range(int(input())):
    m,n,x,y = map(int,input().split())
    print(solve(m,n,x,y))