# 특정 회사끼리는 연결되어 있다. 양방향으로 이동할 수 있다. 
# 1번 회사에서 출발하여 k번 회사를 방문한 뒤 x번 회사로 가는 것이 목표다
# 플로이드 워셜 알고리즘 문제

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print('-1')
else:
    print(distance)