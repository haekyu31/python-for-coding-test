# n가지 종류의 화폐 개수를 최소한으로 이용해서 가치의 합이 m이 되도록
# 그리디 문제와 비슷하지만 화폐 단위가 배수가 아니기 때문에 그리디로 풀 수 없다. 
# 작은 금액부터 큰 금액까지 확인하며 차례대로 만들 수 있는 최소한의 화폐 개수를 찾는다. 

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

d = [10001] * (m + 1)

d[0] = 0

for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])