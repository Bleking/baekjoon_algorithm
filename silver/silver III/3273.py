# 백준 3273번 두 수의 합 실버 3

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()

left, right = 0, N-1
answer = 0
while left < right:
  if arr[left] + arr[right] < x:
    left += 1
  elif arr[left] + arr[right] > x:
    right -= 1
  elif arr[left] + arr[right] == x:
    answer += 1
    right -= 1

print(answer)
