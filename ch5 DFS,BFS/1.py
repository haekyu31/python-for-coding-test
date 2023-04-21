# 팩토리얼 구현

# 반복으로 구현
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
# 재귀로 구현
def factorial2(n):
    if n <= 1:      # 종료조건을 걸어줘야 한다. 
        return 1
    return n * factorial2(n-1)


    