# 계수 정렬 count sort
# 특정조건에서만 사용가능한 정렬 알고리즘
# 별도의 리스트를 선언하고 그 안에 정렬에 대한 정보를 담는다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4 ,8, 0, 5, 2]
count= [0]*(max(array) +1)

for i in range(len(array)):
    count[array[i]] +=1 # 각 데이터에 해당하는 인덱스의 값 증가
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
        
# 시간복잡도 n + k 