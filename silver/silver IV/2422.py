# 백준 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 실버 4

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
icecreams = [i for i in range(1, N+1)]

nope = set()
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  nope.add((a, b))
  nope.add((b, a))

answer = 0
for x, y, z in combinations(icecreams, 3):
  if (x, y) not in nope and (y, z) not in nope and (x, z) not in nope:
    answer += 1

print(answer)
