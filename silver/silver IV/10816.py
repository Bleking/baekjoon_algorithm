# 백준 10816번 숫자 카드 2 실버 4

import sys
from collections import Counter

N = int(sys.stdin.readline())
cards1 = list(map(int, sys.stdin.readline().split()))
cards1.sort()

M = int(input())
cards2 = list(map(int, sys.stdin.readline().split()))

cards1_counter = Counter(cards1)

answer = [cards1_counter[c] for c in cards2]
print(*answer)
