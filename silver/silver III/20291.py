# 백준 20291번 파일정리 실버3

import sys
from collections import deque

file_queue = deque()
answer = {}

N = int(sys.stdin.readline())
for i in range(N):
  file_queue.append(input().split('.')[1])
  if file_queue[i] not in answer:
    answer[file_queue[i]] = 0
  answer[file_queue[i]] += 1

for idx in sorted(answer.keys()):
    print(idx, answer[idx])
