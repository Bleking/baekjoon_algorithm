# 백준 28066 타노스는 요세푸스가 밉다 실버2

import sys
from collections import deque

sq = deque()  # 청설모 큐
k_queue = deque()

N, K = map(int, sys.stdin.readline().split())

sq = deque([i+1 for i in range(N)])  # 청설모 큐

while len(sq) >= 1:  
  if len(sq) < K:
    break
  
  sq.append(sq.popleft())
  for k in range(K-1):
    sq.popleft()
  
  if len(sq) >= 2:
    continue

print(sq[0])
