# 수열을 큰 수부터 작은 수의 순서로 정렬
n = int(input())
array = [int(input()) for _ in range(n)]
array.sort(reverse = True)
for i in array:
    print(i, end = ' ')