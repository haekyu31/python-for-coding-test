# n x m의 얼음틀이 있다. 구멍이 뚫린 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 한번에 만들 수 있는 아이스크림의 개수를 출력하시오

# 문제 해결 알고리즘 그래프의 0인 지점을 서로 연결하여 아직 0인 부분을 찾고 방문했다면 1로 표시한다. 더이상 탐색할 곳이 없다면 얼음 1개를 추가한다. 이 과정을 전체 그래프를 돌면서 진행한다. 

n, m  = map(int, input().split())

# 2차원 리스트 맵 정보 받기
graph = [list(map(int, input().split())) for i in range(n)]

# dfs로 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y > m:   
        return False
    # 방문한 적이 없다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:   # True 인곳부터 탐색을 시작
            result += 1         # 깊이 탐색을 한다음 count 1 증가
print(result)
