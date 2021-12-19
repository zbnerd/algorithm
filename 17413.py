import sys
from collections import deque

input = sys.stdin.readline

string = input()
string = string.replace('<','!<').replace('>','>!').replace('\n','')
arrow_split = string.split('!')
answer = []

for sentence in arrow_split:
    if '<' in sentence:
        answer.append(sentence)
    else :
        space_split = sentence.split(' ')
        for sentence2 in space_split:
            answer.append(sentence2[::-1])

ans_string = ' '.join(answer)
print(ans_string.replace(' <','<').replace('> ','>'))

if not answer:
    print(string[::-1])
