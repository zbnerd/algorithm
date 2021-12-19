import sys
from collections import defaultdict

#input = sys.stdin.readline

n = int(input())
books = defaultdict(int)
books_list = []
best_sellor = ''

for i in range(n):
    books[input()]+=1
    
for k,v in books.items():
    books_list.append((v,k))

books_list_sort = sorted(books_list,key=lambda x : (-x[0],x[1]))
    
print(books_list_sort[0][1])