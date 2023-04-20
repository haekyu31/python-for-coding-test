# 체스판은 8 x 8 나이트는 L자 형태로만 이동할 수 있다. 좌표를 벗어날 수는 없다.
# 나이트가 이동할 수 있는 경우의 수를 출력
# 행 위치는 1에서 8 열 위치는 a부터 h

# 현재 위치 
knight = input()
row = int(knight[1])
col = int(ord(knight[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 방향 8가지
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:      # 8방향에 대해서 모두 이동한다음
    nrow = row + step[0]
    ncol = col + step[1]
    # 좌표 안에 들어갈 경우 count를 1 늘이는 방법
    if nrow >= 1 and nrow <= 8 and ncol >=1 and ncol <= 8:
        result += 1
print(result)