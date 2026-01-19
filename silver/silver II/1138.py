# 백준 1138번 한 줄로 서기 실버 2

import sys

N = int(sys.stdin.readline())
left = list(map(int, sys.stdin.readline().split()))
answer = [0] * N

for i in range(N):
  count = 0
  for j in range(N):
    if answer[j] == 0 and count < left[i]:
      count += 1
    elif answer[j] == 0 and count == left[i]:
      answer[j] = i + 1
      break

print(*answer)
