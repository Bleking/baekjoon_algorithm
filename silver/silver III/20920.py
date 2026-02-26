# 백준 20920번 영단어 암기는 괴로워 실버 3

import sys

N, K = map(int, sys.stdin.readline().split())
dictionary = {}
for i in range(N):
  word = sys.stdin.readline().strip()
  if len(word) >= K:
    if word not in dictionary:
      dictionary[word] = 1
    else:
      dictionary[word] += 1

answer = sorted(dictionary.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for a in answer:
  print(a[0])
