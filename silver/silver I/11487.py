# 백준 11497번 통나무 건너뛰기 실버1

import sys

T = int(sys.stdin.readline())

for t in range(T):
  N = int(sys.stdin.readline())
  logs = list(map(int, sys.stdin.readline().split()))
  logs = sorted(logs)

  logs_rearanged = [0] * N

  index_even, index_odd = 0, 0
  for n in range(N):
    if n % 2 == 0:
      logs_rearanged[index_even] = logs[n]
      index_even += 1
    elif n % 2 == 1:
      logs_rearanged[-1 - index_odd] = logs[n]
      index_odd += 1

  answer = abs(logs_rearanged[0] - logs_rearanged[-1])
  for i in range(1, N):
    dif = abs(logs_rearanged[i] - logs_rearanged[i-1])

    if dif > answer:
      answer = dif

  print(answer)
