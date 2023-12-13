text1 = input()
text2 = input()
LCS_dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]  # 행이 첫 번째 수열, 열이 두 번째 수열이어야 한다.

for i in range(1, len(text1) + 1):
  for j in range(1, len(text2) + 1):
    if text1[i-1] == text2[j-1]:
      LCS_dp[i][j] = LCS_dp[i-1][j-1] + 1
    else:
      LCS_dp[i][j] = max(LCS_dp[i-1][j], LCS_dp[i][j-1])
      
print(LCS_dp[-1][-1])
