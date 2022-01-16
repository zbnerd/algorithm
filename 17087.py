import math
import sys

input = sys.stdin.readline

n, s = map(int,input().split())
a = list(map(int,input().split()))

dist = [abs(s-a[i]) for i in range(len(a))]
print(math.gcd(*dist))