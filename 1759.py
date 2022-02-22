l, c = map(int, input().split())
vowel = {'a','e','i','o','u'}

def make_password(max_length, alpha, password, i):
    if len(password) > max_length:
        return

    equal_length = len(password) == max_length
    atLeast_vowel_1 = len(set(password) & vowel)  >= 1
    atLeast_consonant_2 = len(set(password) - vowel) >= 2

    if equal_length and atLeast_vowel_1 and atLeast_consonant_2:
        print(password)
        return
   
    try:
        make_password(max_length, alpha, password+alpha[i], i+1)
        make_password(max_length, alpha, password, i+1)
    except:
        pass

    
make_password(l, sorted(list(input().split())), '', 0)