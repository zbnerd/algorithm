import sys

input = sys.stdin.readline

a,b = 0,1
n = int(input())
# 피사노주기를 이용하면 되는 문제
# 주기 공식 10^n으로 나눈 나머지의 피사노 주기는
# 15*10^(n-1)
# 100만은 10^6 피사노 주기는 15*10^5
n = n % 1500000

for i in range(n):
    a,b = b%1000000, (a+b)%1000000

print(a)