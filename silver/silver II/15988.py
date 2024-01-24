import sys

dp = [1, 2, 4]

T = int(sys.stdin.readline())
for t in range(T):
  n = int(sys.stdin.readline())

  for i in range(len(dp) + 1, n+1):
    dp.append((dp[-3] + dp[-2] + dp[-1])%1000000009)
  print(dp[n-1])
