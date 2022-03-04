import sys

input = sys.stdin.readline

#가로, 세로 입력받기
n, m = map(int, input()[:-1].split())

#1차원배열을 2차원배열로 변환하는 함수
def reshape_to2d(a):
    b = []
    start = 0
    end = m
    
    while end <= (n*m):
        b.append(list(a[start:end]))
        start += m
        end += m

    return b

#숫자가 적혀있는 직사각형 종이 입력
board = []
for _ in range(n):
    board.append(list(map(int,list(input()[:-1]))))

#최댓값 저장 변수
mx = 0

#1부터 2^(n*m)까지 2진수 비트를 모두 순회
for b in range(2**(n*m)):
    #종이조각의 합 저장 변수
    sigma = 0

    #i에 해당하는 비트를 나타내는데 자릿수는 m*n자릿수로 맞추고 2차원배열로 변환
    #0은 가로 1은 세로
    bits = str(bin(b))[2:].zfill(n*m)
    bits_2d = reshape_to2d(bits)

    #종이조각의 수 임시저장변수
    tmp = 0

    #가로에 해당하는경우 변수 저장
    for i in range(len(board)):
        for j in range(len(board[i])):
            if bits_2d[i][j] == '0':
                tmp *= 10
                tmp += board[i][j]
    #가로에 해당하지 않는 경우 sigma에 값 더해주고 tmp 초기화
            else :
                sigma += tmp
                tmp = 0

        sigma += tmp
        tmp = 0

    #세로에 해당하는경우를 보기위해 점수 2차원배열과 비트 2차원배열을 전치
    transboard = list(map(list, zip(*board)))
    transbits2d = list(map(list, zip(*bits_2d)))
    
    #세로
    tmp = 0
    for i in range(len(transboard)):
        for j in range(len(transboard[i])):
            if transbits2d[i][j] == '1':
                tmp *= 10
                tmp += transboard[i][j]
                
            else :
                sigma += tmp
                tmp = 0

        sigma += tmp
        tmp = 0

    mx = max(mx, sigma)

print(mx)