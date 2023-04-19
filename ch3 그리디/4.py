# n이 1이 될 때까지 1을 빼거나 k로 나눈다. 최소 수행횟수를 구하라

n, k = map(int, input().split())
result = 0


# 시간 초과가 발생

# # 나눌 수 있다면 최대한 나누고 나눌 수 없다면 1을 빼준다. 그리디 알고리즘
# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
#     n //= k
#     result += 1
# # 나눌 수 없을 때 1을 계속해서 빼준다.
# while n > 1:
#     n -= 1
#     result += 1
    
# print(result)

# n이 k의 배수가 되도록 한번에 빼는 과정
while True:
    target = (n//k) * k
    result += (n-target)
    
    n = target
    
    if n < k:
        break
    result += 1
    n //= k
    
result += -1
print(result)
    