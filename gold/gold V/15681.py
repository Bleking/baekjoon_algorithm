# 백준 15681번 트리와 쿼리 골드 5

import sys
sys.setrecursionlimit(10**6)

N, R, Q = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
  u, v = map(int, sys.stdin.readline().split())
  tree[u].append(v)
  tree[v].append(u)

dp = [1] * (N+1)
visited = [False] * (N+1)

def dfs(tree, node, visited):
  visited[node] = True

  for next in tree[node]:
    if visited[next] == False:
      dfs(tree, next, visited)
      dp[node] += dp[next]

dfs(tree, R, visited)

for _ in range(Q):
  u = int(sys.stdin.readline())
  print(dp[u])
