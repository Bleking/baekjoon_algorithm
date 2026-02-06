# 백준 9095번 	1, 2, 3 더하기 실버 3

import sys

T = int(sys.stdin.readline())

for t in range(T):
  n = int(sys.stdin.readline())

  if n == 1:
    answer = 1
  elif n == 2:
    answer = 2
  elif n == 3:
    answer = 4
  else:
    dp = [0] * (n+1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for i in range(4, n+1):
      dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    answer = dp[-1]
    
  print(answer)
