# 백준 1181번 단어 정렬 실버 5

import sys

N = int(sys.stdin.readline())
word_list = []
for i in range(N):
    word_list.append(sys.stdin.readline().strip())

word_list = list(set(word_list))
word_list.sort(key=lambda x: (len(x), x))

for w in word_list:
    print(w)
