# 백준 11497번 통나무 건너뛰기 실버 1

import sys

T = int(sys.stdin.readline())

for t in range(T):
  N = int(sys.stdin.readline())
  logs = list(map(int, sys.stdin.readline().split()))
  logs = sorted(logs)

  logs_rearanged = [0] * N
  index_even, index_odd = 0, 0
  for i in range(N):
    if i % 2 == 0:
      logs_rearanged[index_even] = logs[i]
      index_even += 1
    if i % 2 == 1:
      logs_rearanged[-1 - index_odd] = logs[i]
      index_odd += 1

  dif_list = [abs(logs_rearanged[i] - logs_rearanged[i-1]) for i in range(1, N)]
  dif_list.append(abs(logs_rearanged[0] - logs_rearanged[-1]))

  print(max(dif_list))
