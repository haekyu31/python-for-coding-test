# a, b 두 배열은 n개의 원소로 구성되어있고 최대 k번의 바꿔치기를 통해 a의 모든 원소의합이 최대가 되도록 하는 것이다.

n, k = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

# a에서 가장 작은 수를 골라 b의 가장 큰 수와 교환 단 a의 가장 작은수가 b의 가장 큰 수보다 작을 때만
# a를 정렬하고  b는 역순으로 정렬하여 서로 비교

a.sort()
b.sort(reverse = True)
for i in range(k):
    if a[i] < b[i]:
        a[i] , b[i] = b[i], a[i]
    else:
        break
print(sum(a))