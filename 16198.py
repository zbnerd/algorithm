import sys

input = sys.stdin.readline

def is_terminated(a):

    for b in range(1,len(a)-1):
        if not a[b]:
            return False

    return True

def back_tracking(i, e):
    global energy

    energy = max(energy, e)

    if is_terminated(removed):
        e += w[0]*w[-1]
        energy = max(energy, e)
        return

    left, right = i, i
    while 0 <= left < n:
        left -= 1
        
        if not removed[left]:
            break

    while 0 <= right < n:
        right += 1
        
        if not removed[right]:
            break

    gather = w[left]*w[right]

    for j in range(1,n-1):
        if not removed[j]:
            removed[j] = True
            back_tracking(j,e+gather)
            removed[j] = False
            

n = int(input())
w = list(map(int, input().split()))
energy = 0
removed = [False] * n

for i in range(1,n-1):
    removed[i] = True
    back_tracking(i,0)
    removed[i] = False

print(energy)