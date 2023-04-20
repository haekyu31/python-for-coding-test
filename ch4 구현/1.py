# N x N 의 공간, 시작좌표는 (1, 1) A가 쵲ㅇ적으로 도착할 지점의 좌표를 출력
n = int(input())
moves = list(input().split())

# 순서대로 움직이면서 좌표가 벗어나게 되면 무시하는 방식으로 

x, y = 1, 1

# 이동방향 설정 L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# move에 따라 이동
for move in moves:
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx >n or ny < 1 or ny > n:
        continue        # 공간 범위를 벗어나면 무시
    x, y = nx, ny
print(x, y)
            
