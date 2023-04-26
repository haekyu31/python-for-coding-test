# 피보나치 수열 재귀적
d = [0] * 100

# 탑다운 방식
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# 바텀업 방식
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    