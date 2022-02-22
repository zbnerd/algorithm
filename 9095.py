def go(count, sum, goal):
    count = 0
    if sum > goal:
        return 0
    if sum == goal:
        return 1

    for i in range(1,4):
        count += go(count+1, sum+i, goal)

    return count

for _ in range(int(input())):
    print(go(0, 0, int(input())))