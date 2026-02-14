# 백준 2110번 공유기 설치 골드 4

import sys

N, C = map(int, sys.stdin.readline().split())

houses = []
for _ in range(N):
  houses.append(int(sys.stdin.readline()))
houses.sort()

pl, pr = 1, houses[N-1] - houses[0]

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2
  current = houses[0]  # 첫 번째 집에는 공유기 무조건 설치  # 주의!!
  cnt = 1  # 공유기 개수는 최소 1개
  for i in range(1, N):
    if houses[i] >= current + pc:  # 공유기가 현재 설치된 위치의 거리까지 커버를 못하면
      cnt += 1  # 공유기 하나 더 설치
      current = houses[i]  # 현재 위치에 공유기 설치

  if cnt >= C:  # 현재까지의 공유기 개수가 필요한 개수를 넘어서거나 만족하면
    pl = pc + 1
    answer = pc
  else:  # 현재까지의 공유기 개수가 필요한 개수를 만족하지 못하면
    pr = pc - 1

print(answer)
