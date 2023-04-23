# 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열
# 선택정렬 selection sort
# 가장 작은 데이터를 맨 앞의 데이터와 바꾸고 그다음 작은 데이터를 두번째 데이터와 바꾸는 과정을 반복한다. 
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
print(array)


# 시간복잡도 n2