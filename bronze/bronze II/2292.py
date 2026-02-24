# 백준 2292번 벌집 브론즈 1

import sys

N = int(sys.stdin.readline())

room = 1
layer = 1

while N > room:
    room += 6*layer
    layer += 1

print(layer)
