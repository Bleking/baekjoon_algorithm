# 백준 13417번 카드 문자 실버3

import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
  N = int(sys.stdin.readline())
  cards = list(map(str, sys.stdin.readline().strip().split()))
  cards = deque(cards)
  first_card = cards[0]

  answer = deque()
  answer.append(first_card)

  for i in range(1, N):
    if cards[i] > answer[0]:
      answer.append(cards[i])
    else:
      answer.appendleft(cards[i])

  print(''.join(answer))
