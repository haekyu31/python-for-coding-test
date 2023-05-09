# 숫자로만 이루어진 문자열 S 가장 큰 수를 구하는 프로그램 계산은 왼쪽부터 순서대로 이루어진다.

# 문제해결 알고리즘 곱하기만 하면 가장 큰 수가 나오지만 0이나 1이 들어간 경우에는 0또는 1을 더하기 처리해야 한다.

n = input()

result = int(n[0])

for i in range(1, len(n)):
    num = int(n[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)