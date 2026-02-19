# 백준 17218번 비밀번호 만들기 골드 4

import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

m, n = len(str1), len(str2)

dp = [[''] * (n+1) for _ in range(m+1)]

for i in range(1, m+1):
  for j in range(1, n+1):
    if str1[i-1] == str2[j-1]:
      dp[i][j] = dp[i-1][j-1] + str1[i-1]
    else:
      if len(dp[i-1][j]) < len(dp[i][j-1]):
        dp[i][j] = dp[i][j-1]
      else:
        dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
