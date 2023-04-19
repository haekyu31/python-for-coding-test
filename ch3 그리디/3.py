# 각 행마다 가장 작은 수를 찾은 다음 가장 큰 수를 찾는 것

n, m = map(int, input().split())
graph = [[int(i) for i in input().split()] for _ in range(n)]

result = 0

for i in range(n):
    min_value = min(graph[i])       # i행에서 가장 작은 수를 찾기
    result = max(result, min_value) # result와 min_value중 가장 큰 수를 찾기
    
print(result)