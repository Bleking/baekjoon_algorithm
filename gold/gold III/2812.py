# 백준 2812번 크게 만들기 골드 3

import sys

N, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))

remaining_k = K
stack = [num[0]]
for i in range(1, N):
  if remaining_k > 0:
    while stack and num[i] > stack[-1] and remaining_k > 0:  # while까진 잘 생각했는데, 조건을 더 생각했어야
      stack.pop()
      remaining_k -= 1
  stack.append(num[i])

if remaining_k > 0:  # 이거 안해주면 오답 나옴
    stack = stack[:-remaining_k]

answer = int(''.join(map(str, stack)))
print(answer)
