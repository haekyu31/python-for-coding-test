# 신장 트리 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# 크루스칼 알고리즘 최소한의 비용으로 신장트리를 찾아야 할때 예를 들어 모든 도시를 서로 연결될수 있도록 도로를 설치하는 경우

# 간선 데이터를 비용에 따라 오름차순으로 정렬한다
# 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
# 모든 간선에 대해서 반복한다. 

# 최종 신장트리는 노드의 개수 - 1 과 같다는 특징이 있다.

# 간선과 비용을 정렬수행한다. 가장 짧은 간선을 선택한다. union 함수를 호출 그 다음으로 작은 간선을 선택, 동일한 집합에 포함된 경우 union함수를 호출하지 않는다.

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v + 1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

for i in range(1, v+1):
    parent[i] = i
    
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)