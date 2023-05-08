# 선수강의가 있는 경우 선수강의를 먼저 들어야만 해당 강의를 들을 수 있다. 
# 동시에 여러개의 강의를 들을 수 있다. 

# 각 노드에 인접한 노드를 확인 할때 더 오래걸리는 시간값을 저장하서 결과 테이블을 갱신하는 방식

from collections import deque
import copy

v = int(input())
indegree = [0] * (v +1)
graph = [[] for i in range(v+1)]

# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)
        
# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1, v+1):
        print(result[i])
        
topology_sort()