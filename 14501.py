n = int(input())
Ti = [0]
Pi = [0]
answer = 0

for _ in range(n):
    t, p = map(int, input().split())
    Ti.append(t)
    Pi.append(p)
    
def counsel(day, income):
    global answer
    
    if day == n+1:
        if answer < income:
            answer = income

    if day > n+1:
        return

    try:
        counsel(day+1, income)
        counsel(day+Ti[day], income+Pi[day])
    except :
        pass

counsel(1,0)
print(answer)