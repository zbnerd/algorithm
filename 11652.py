from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
count_of_cards = defaultdict(int)
for i in range(len(cards)):
    count_of_cards[cards[i]] += 1

print(sorted(list(count_of_cards.items()), key = lambda x:(x[1],-x[0]), reverse=True)[0][0])