# 백준 15662번 톱니바퀴 (2) 골드 5

import sys
from collections import deque

T = int(sys.stdin.readline())

gears = []
gears = [deque([0, 0, 0, 0, 0, 0, 0, 0])]
for _ in range(T):
  gears.append(deque(list(map(int, sys.stdin.readline().strip()))))
gears.append(deque([0, 0, 0, 0, 0, 0, 0, 0]))  # => 1, N+1

K = int(sys.stdin.readline())
for _ in range(K):
  num, d = map(int, sys.stdin.readline().split())

  # 각 톱니바퀴의 회전 방향 결정: 0 -> 회전 X, 1 -> 시계 방향 회전, -1: 반시계 방향 회전
  rotate = [0] * (T+1)
  rotate[num] = d

  # 현재 톱니바퀴에서부터 오른쪽 연쇄 확인
  for i in range(num, T):
    if gears[i][2] != gears[i+1][6]:  # 맞닿은 톱니가 다르면
      rotate[i+1] = -rotate[i]  # 반대 방향으로 회전
    else:
      break

  # 현재 톱니바퀴에서부터 왼쪽 연쇄 확인
  for i in range(num, 1, -1):
    if gears[i][6] != gears[i-1][2]:  # 맞닿은 톱니가 다르면
      rotate[i-1] = -rotate[i]  # 반대 방향으로 회전
    else:
      break

  # 일괄 회전
  for i in range(1, T+1):
    if rotate[i] == 1:
      gears[i].appendleft(gears[i].pop())
    elif rotate[i] == -1:
      gears[i].append(gears[i].popleft())

answer = 0
for i in range(1, T+1):
  if gears[i][0] == 1:
    answer += 1

print(answer)
