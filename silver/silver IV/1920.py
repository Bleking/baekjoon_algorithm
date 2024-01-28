import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = sorted(A)

M = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

def binary_search(a, key):
  pl, pr = 0, len(a) - 1

  while True:
    pc = (pl + pr) // 2

    if a[pc] == key:
      return True
    elif a[pc] < key:
      pl = pc + 1
    elif a[pc] > key:
      pr = pc - 1
    
    if pl > pr:
      break
  
  return False

for i in range(M):
  if binary_search(A, num_list[i]):
    print(1)
  else:
    print(0)
