# 위상 정렬
# 순서가 정해져 있는 일련의 작업을 차례대로 수행해야 할 때 , 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

# 진입차수가 0인 노드를 큐에 넣는다.
# 큐가 빌 때까지 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다 반복
# 모든 원소 방문전 큐가 빈다면 사이클이 존재한다고 볼 수 있다. 

from collections import deque

# 노드의 개수와 간선의 개수를 입력
v, e  = map(int, input().split())

# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # a에서 b 로 이동가능
    # 진입차수를 1 증가
    indegree[b] += 1    
    
# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    # 처음 시작할 때는 진입차수가 0 인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    
    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in result:
        print(i, end = ' ')

topology_sort()
            
    