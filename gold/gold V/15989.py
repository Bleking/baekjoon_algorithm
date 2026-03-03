# 백준 15989번 1, 2, 3 더하기 4 골드 5

import sys

dp = [1] * 10001

for i in range(2, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]

T = int(sys.stdin.readline())
for t in range(T):
    print(dp[int(sys.stdin.readline())])
