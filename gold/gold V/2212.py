# 백준 2212번 센서 골드5

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensors = sorted(list(map(int, sys.stdin.readline().split())))

distances = []
for i in range(1, N):
  distances.append(sensors[i] - sensors[i-1])

distances = sorted(distances)

print(sum(distances[:N-K]))
