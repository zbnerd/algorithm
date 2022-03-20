import sys

input = sys.stdin.readline


n = int(input())
alpha_nums = [input()[:-1] for _ in range(n)]
num_alpha_pair = dict()

# 숫자 알파벳 짝 딕셔너리 초기화
for string in alpha_nums:
    for i in range(len(string)-1,-1,-1):
        num_alpha_pair[string[i]] = 0

# 숫자 알파벳 짝 값 지정
for string in alpha_nums:
    ten_power = 1
    for i in range(len(string)-1,-1,-1):
        num_alpha_pair[string[i]] += ten_power*(10**(len(string)-i-1))
        
item = list(num_alpha_pair.items())

# 숫자 알파벳 짝 value를 기준으로 내림차순 정렬
item.sort(key = lambda x : x[1], reverse = True)
value = 0

# 정답 구하기
for i in range(len(item)):
    value += (item[i][1] * (9-i))

print(value)