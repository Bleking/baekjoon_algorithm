from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
visited = [[False] * N for _ in range(N)]

dh = [0, 0, 1, -1]
dw = [1, -1, 0, 0]


def BFS(graph, N, h, w):
    queue = deque()
    queue.append([h, w])
    count = 1

    while queue:
        h, w = queue.popleft()

        for i in range(4):
            nh = h + dh[i]
            nw = w + dw[i]

            if 0 <= nh < N and 0 <= nw < N:
                if graph[nh][nw] == 1 and not visited[nh][nw]:
                    visited[nh][nw] = True
                    queue.append([nh, nw])
                    count += 1
    return count


ans = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            ans.append(BFS(graph, N, i, j))

ans.sort()
print(len(ans))
for idx in range(len(ans)):
    print(ans[idx])
