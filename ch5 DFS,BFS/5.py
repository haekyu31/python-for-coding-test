# n x m 크기의 미로 시작위치는 (1, 1), 출구는 (n, m) 길이 있는 부분은 1로 길이 없는 부분은 0으로 표시 탈출하기 위해서 최소한으로 움직이는 칸의 갯수를 구하시오
# 칸을 셀때 시작칸 마지막칸 모두 포함해서 계산한다. 

from collections import deque

n,m  = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:      # graph의 index형태로 계산할때 
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 이전거리에서 1 증가한 거리로 표시
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))
                