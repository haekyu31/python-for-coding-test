# 팀결성 
# 0번부터 N번까지 N + 1개의 팀이 존재한다. 팀합치기는 두팀을 합치는 연산, 같은 팀 여부는 학생이 같은 팀에 속하는지 확인하는 연산

# 서로소 집합 알고리즘 문제

# 특정 원소가 속한 집합을 찾기
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
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

# 부모 테이블 상에서 , 부모를 자기 자신으로 초기화
for i in range(0, n+1):
    parent[i] = i
    
# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    # 합집합인 경우
    if oper == 0:
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')