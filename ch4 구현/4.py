# N x M 칸은 육지 또는 바다
# 캐릭터는 바다라는 갈 수 없다. 
# 캐릭터는 현재 방향기준 왼쪽방향부터 갈 곳을 정한다
# 왼쪽 방향으로 가보지 않았다면 왼쪽으로 한 칸 가보지 않은 칸이 없다면 왼쪽으로 회전만
# 모두 가본 칸이거나 바다라면 방향유지한채로 1 칸 뒤로 이동한다
# 뒤쪽 방향도 바다라면 움직임을 멈춘다.

# 전형적인 시뮬레이션 문제

# n x m 맵 생성
n, m = map(int, input().split())
# 캐릭터의 위치와 바라보는 방향
x, y, direction = map(int, input().split())
# 전체 맵에 대한 정보
graph = [[int(i) for i in input().split()] for _ in range(n)]

# 방문 정보에 대해 저장하기 위한 맵
visited = [[0]* m for _ in range(n)]
# 캐릭터 현재위치 방문 처리
visited[x][y] = 1

# 방향 설정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# 시뮬레이션 구현
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 이후 가보지 않은 칸이 존재하면 이동
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 이후 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈수 있는경우 이동하기
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤에 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
print(count)