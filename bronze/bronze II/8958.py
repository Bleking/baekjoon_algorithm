# 백준 8958번 OX퀴즈 브론즈 2

import sys

T = int(sys.stdin.readline())

for t in range(T):
  S = sys.stdin.readline().strip()
  answer = 0
  cnt = 0
  for i in range(len(S)):
    if S[i] == 'O':
      cnt += 1

    elif S[i] == 'X':
      cnt = 0
    
    answer += cnt

  print(answer)
