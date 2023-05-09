# n개의 동전을 가직 만들 수 없는 양의 정수 금액중 최솟값을 구하는 프로그램
# 동전 개수를 나타내는 n, 각 동전의 화폐 단위를 나타내는 n개의 자연수

n = int(input())
coins = [int(i) for i in input().split()]

# 문제 해결 알고리즘
# 가장 작은 것부터 만들 수 있는지 확인 

coins.sort()
target = 1
for coin in coins:
    if coin > target:
        break
    else:
        target += coin
print(target)