# 백준 1940번 주몽 실버 4

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ingredients = list(map(int, sys.stdin.readline().split()))
ingredients.sort()

left, right = 0, N-1
answer = 0
while left < right:
  if ingredients[left] + ingredients[right] < M:
    left += 1
  elif ingredients[left] + ingredients[right] > M:
    right -= 1
  elif ingredients[left] + ingredients[right] == M:
    answer += 1
    right -= 1

print(answer)
