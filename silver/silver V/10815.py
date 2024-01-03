import sys

N = int(sys.stdin.readline())
cards1 = list(map(int, sys.stdin.readline().split()))
cards1.sort()

M = int(sys.stdin.readline())
cards2 = list(map(int, sys.stdin.readline().split()))

is_exist = []

def binary_search(arr, key):
  pl, pr = 0, len(arr) - 1  # 0, N - 1

  while True:
    pc = (pl + pr) // 2

    if arr[pc] == key:
      return True
    elif arr[pc] < key:
      pl = pc + 1
    elif arr[pc] > key:
      pr = pc - 1
    
    if pl > pr:
      break
  
  return False


for i in range(M):
  if binary_search(cards1, cards2[i]) == True:
    is_exist.append(1)
  else:
    is_exist.append(0)

print(*is_exist)
