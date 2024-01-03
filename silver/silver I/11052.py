import sys

N = int(sys.stdin.readline())
P = [0] + list(map(int, sys.stdin.readline().split()))

cards_dp = [0]
max_value = 0
for i in range(1, N+1):
  for j in range(i):
    max_value = max(max_value, P[i-j] + cards_dp[j])
  cards_dp.append(max_value)

print(cards_dp[N])
