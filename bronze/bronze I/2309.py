# 백준 2309번 일곱 난쟁이 브론즈 1

import sys

dwarfs = []
for _ in range(9):
  dwarfs.append(int(sys.stdin.readline()))

temp = sum(dwarfs) - 100
for i in range(8):
  for j in range(i+1, 9):
    if dwarfs[i] + dwarfs[j] == temp:
      first, second = dwarfs[i], dwarfs[j]

dwarfs.remove(first)
dwarfs.remove(second)
dwarfs.sort()

for d in dwarfs:
  print(d)
