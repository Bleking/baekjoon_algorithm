# 백준 3055번 탈 골드 4

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
    row = list(sys.stdin.readline().strip())
    graph.append(row)
    
    if 'S' in row:
        s1, s2 = i, row.index('S')
    if 'D' in row:
        d1, d2 = i, row.index('D')

water = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
            water.append((i, j))

def hedgehog_bfs(graph, r, c, visited, water):
    queue = deque()
    queue.append((r, c))
    
    visited[r][c] = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        # 물 확산
        for _ in range(len(water)):
            wr, wc = water.popleft()
            for d in range(4):
                nwr = wr + dr[d]
                nwc = wc + dc[d]
                
                if 0 <= nwr < R and 0 <= nwc < C:
                    if graph[nwr][nwc] == '.':
                        graph[nwr][nwc] = '*'
                        water.append((nwr, nwc))
        
        # 고슴도치 이동
        for _ in range(len(queue)):
            r, c = queue.popleft()
            
            # 목적지 도착 체크
            if r == d1 and c == d2:
                return visited[r][c]
            
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                
                if 0 <= nr < R and 0 <= nc < C:
                    if visited[nr][nc] == -1:
                        # '.'이거나 'D'인 경우만 이동 가능
                        if graph[nr][nc] == '.' or graph[nr][nc] == 'D':
                            visited[nr][nc] = visited[r][c] + 1
                            queue.append((nr, nc))
    
    return -1

visited = [[-1] * C for _ in range(R)]

answer = hedgehog_bfs(graph, s1, s2, visited, water)

if answer == -1:
    print('KAKTUS')
else:
    print(answer)
