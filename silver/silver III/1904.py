N = int(input())

dp = [0] * (N+1)
dp[0], dp[1] = 1, 2

for i in range(2, N):
  dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[N-1])
