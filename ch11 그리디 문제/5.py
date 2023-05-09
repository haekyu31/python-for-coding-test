# a, b 서로 무게가 다른 볼링공을 고른다. 공은 총 n개가 있고 무게는 1부터 m까지 존재한다.

n, m = map(int, input().split())
weights = [int(i) for i in input().split()]

# 문제 해결 알고리즘
# 무게별로 정렬한 다음에 자신보다 큰 무게의 경우만 확인한다.


# 이중 for loop로 비효율적
# weights.sort()
# result = 0

# for i in range(n-1):
#     for j in range(i+1, n):
#         if weights[i] != weights[j]:
#             result += 1
# print(result)

# a를 기준으로 b는 a보다 높은 것만 선택한다고 설정한다.
array = [0] * 11
for i in weights:
    array[i] += 1
    
result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)
