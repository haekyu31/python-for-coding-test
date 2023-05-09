# 모험가 n이 주어진다
# 각 모함가의 공포도는 n이하의 자연수로 주어진다 
# 공포도가 n인 모함가는 반드시 n명 이상으로 구성한 그룹에 참여해야 한다.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력

n = int(input())
array = list(map(int, input().split()))

# 문제 해결 알고리즘 정렬한 뒤 순서대로 조건에 맞게 그룹을 만든다. 남은 모험가는 계산하지 않는다. 

array.sort()

result = 0
count  = 0

for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0
print(result)