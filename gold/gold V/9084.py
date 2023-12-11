T = int(input())  # 테스트 케이스 개수

for t in range(T):
  N = int(input())  # 동전의 가지 수
  coins = list(map(int, input().split()))  # 동전의 각 금액

  M = int(input())  # N가지 동전으로 만들어야 할 금액
  coin_dp = [0] * (M+1)
  coin_dp[0] = 1

  for c in coins:
    for i in range(M+1):
      if i >= c:
        coin_dp[i] += coin_dp[i-c]
  print(coin_dp[M])
