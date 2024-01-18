import sys

T = int(sys.stdin.readline())

for t in range(T):
  N = int(sys.stdin.readline())
  note1 = list(map(int, sys.stdin.readline().split()))
  note1.sort()

  M = int(sys.stdin.readline())
  note2 = list(map(int, sys.stdin.readline().split()))

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

  is_match = [0] * M
  for i in range(M):
    if binary_search(note1, note2[i]) == True:
      is_match[i] = 1
    else:
      is_match[i] = 0

  for idx in range(M):
    print(is_match[idx])
