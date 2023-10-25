from collections import deque

N = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

grid = [list(input()) for _ in range(N)]
grid_rg = [['R' if element == 'G' else element for element in row] for row in grid]
visited = [[False] * N for _ in range(N)]
visited_rg = [[False] * N for _ in range(N)]

print(grid)
print(grid_rg)


def bfs(x, y, map, visited, colour):
    # count = 1
    num = 0

    queue = deque()
    queue.append([x, y])

    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if (map[nx][ny] == colour) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                    # count += 1
    num += 1

    return num


red = 0
green = 0
blue = 0
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R' and not visited[i][j]:
            red += bfs(i, j, grid, visited, 'R')
        elif grid[i][j] == 'G' and not visited[i][j]:
            green += bfs(i, j, grid, visited, 'G')
        elif grid[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, grid, visited, 'B')

redNgreen = 0
for i in range(N):
    for j in range(N):
        # 적록색약
        if grid_rg[i][j] == 'R' and not visited_rg[i][j]:
            redNgreen += bfs(i, j, grid_rg, visited_rg, 'R')

print(red, green, blue)
print(redNgreen)

print(red + green + blue, redNgreen + blue)
