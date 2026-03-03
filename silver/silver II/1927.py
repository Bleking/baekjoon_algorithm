# 백준 1927번 최소  실버 2

import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for n in range(N):
  x = int(sys.stdin.readline())

  if x == 0:
    if len(heap) == 0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)
