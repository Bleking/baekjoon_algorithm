# 백준 1812번 사탕 실버 4

import sys

N = int(sys.stdin.readline())
candies = []
for _ in range(N):
  candies.append(int(sys.stdin.readline()))

candy = [0] * N

candy[0] = (sum(candies[::2]) - sum(candies[1::2])) // 2
for i in range(1, N):
  candy[i] = candies[i-1] - candy[i-1]

for c in candy:
  print(c)
