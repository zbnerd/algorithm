def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod == 0:
            mod = 4
            n -= 1
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n):
    return convert(n,3)