# 도시 분할 계획
# n 개의 집과 m개의 길로 이루어져 있다. 2개의 분리된 마을로 분할할 계획을 세우고 있다. 

# 2개의 최소 신장 트리를 만들어야 한다. 최소 신장 트리를 찾은 뒤에 최소 신장 간선 중에서 가장 비용이 큰 간선을 제거하는 것이다.

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
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
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
print(result - last)