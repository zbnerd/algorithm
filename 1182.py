import sys

input = sys.stdin.readline

#문제 요구사항 입력받기
n, s = map(int, input().split())
n_list = list(map(int, input().split()))

#부분집합의 합 만족하는 갯수 구하기위한 변수
count = 0

#비트마스크를 이용하여 1부터 2^n까지 순회
for i in range(1, 2**n):
    #i를 이진수로 변환하기. 만약 1이라면 집합에 속해있는것이고 0이면 속해있지않은것
    bits = list(map(int, bin(i)[2:].zfill(n)))
    sigma = 0

    #1을곱하면 부분집합에 속한것이나 마찬가지고 0을곱하면 부분집합에 속하지 않은것이나 마찬가지
    for j in range(n):
        sigma += (n_list[j]*bits[j])

    #부분집합의 합이 만족하면 count 1 증가
    if sigma == s:
        count += 1

print(count)