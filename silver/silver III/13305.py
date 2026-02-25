# 백준 13305번 주유소 실버 3

import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
gas = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(N-1):
  if gas[i] >= gas[i+1]:
    answer += (gas[i] * road[i])
  elif gas[i] < gas[i+1]:
    answer += (gas[i] * road[i])
    gas[i+1] = gas[i]

print(answer)
