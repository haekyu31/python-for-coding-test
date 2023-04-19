n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

# 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙, k번을 초과하여 더해질 수 없는 것이 법칙의 특징
# 그리디 알고리즘 가장 큰 수를 k번 반복하고 두번째로 큰 수 를 한번 더하는 방식으로 

# 시간초과가 발생
# nums.sort()
# first = nums[n-1]
# second = nums[n-2]

# result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# print(result)


nums.sort()
first = nums[n-1]
second = nums[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count)  * first
result += (m-count) * second

print(result)