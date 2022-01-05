#2448 별찍기 -11
import sys

input = sys.stdin.readline

def f(n):
    if n==3:
        arr = [
            [' ',' ','*',' ',' '],
            [' ','*',' ','*',' '],
            ['*']*5
        ]
        
        return arr
    else :
        arr = f(n//2)
        ans = []
        for _ in range(n):
            ans.append([' ']*(2*n-1))
            
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                ans[i][j+n//2] = arr[i][j]
                ans[i+n//2][j] = arr[i][j]
                ans[i+n//2][j+n] = arr[i][j]
            
        return ans
        
for c in f(int(input())):
    print(''.join(c))