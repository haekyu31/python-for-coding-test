# 자른 후의 길이가 m이 되도록 하는 높이의 최댓값을 구하시오
# 파라메트릭 서치 최적화 문제를 결정 문제로 바꾸어 해결하는 기법 
n, m = map(int, input().split())
array = [int(i) for i in input().split()]

# 시작점은 0 끝 점은 가장 긴 떡의 길이로 설정

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid: 
            total += x-mid 
    if total < m:
        end = mid -1
    else:
        result = mid
        start = mid +1 
print(result)