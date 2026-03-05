# 백준 1759번 암호 만들기 골드 5

import sys
from itertools import combinations

L, C = map(int, input().split())
letters = list(map(str, input().split()))
letters.sort()

vowels = ['a', 'e', 'i', 'o', 'u']

for c in combinations(letters, L):
  cnt = 0  # 모음 개수
  for v in vowels:
    if v in c:
      cnt += 1
  
  if cnt >= 1 and L - cnt >= 2:
    print(''.join(c))
