# 백준 1411번 비슷한 단어 실버 2

import sys
from itertools import combinations

N = int(sys.stdin.readline())
words = []
for _ in range(N):
  words.append(sys.stdin.readline().strip())

patterns = []
for word in words:
  pattern = []
  mapping = {}

  cnt = 0
  for w in word:
    if w not in mapping:
      mapping[w] = cnt
      cnt += 1
    pattern.append(mapping[w])

  patterns.append(pattern)

answer = 0
for a, b in combinations(patterns, r=2):
  if a == b:
    answer += 1

print(answer)
