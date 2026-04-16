# 백준 14891번 톱니바퀴 골드 5

import sys
from collections import deque

gears = [
    deque([0, 0, 0, 0, 0, 0, 0, 0])
]
for _ in range(4):
  gears.append(deque(list(map(int, sys.stdin.readline().strip()))))
gears.append(deque([0, 0, 0, 0, 0, 0, 0, 0]))

rotation = [0] * 6  # 각 톱니바퀴의 회전 방향
K = int(sys.stdin.readline())
for _ in range(K):
  num, dir = map(int, sys.stdin.readline().split())
  
  # 회전 방향 결정하기
  rotation[num] = dir
  for i in range(num, 0, -1):  # 앞쪽 톱니바퀴 회전 방향
    if gears[i][6] != gears[i-1][2]:
      rotation[i-1] = -rotation[i]
  for i in range(num, 5):  # 뒤쪽 톱니바퀴 회전 방향
    if gears[i][2] != gears[i+1][6]:
      rotation[i+1] = -rotation[i]

  # 톱니바퀴 회전 적용하기
  for i in range(1, 4+1):
    if rotation[i] == 1:
      gears[i].appendleft(gears[i].pop())
    elif rotation[i] == -1:
      gears[i].append(gears[i].popleft())

  rotation = [0] * 6  # 완료되고 나면 회전 초기화

answer = 0
if gears[1][0] == 1:
  answer += 1
if gears[2][0] == 1:
  answer += 2
if gears[3][0] == 1:
  answer += 4
if gears[4][0] == 1:
  answer += 8

print(answer)
