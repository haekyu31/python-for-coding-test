# 삽입 정렬 insertion sort
# 데이터를 확인하면서 데이터를 적절한 위치에 삽입하는 방법
# 첫번째 데이터는 정렬되어 있다고 판단하고 두번째 데이터부터 확인한다. 
# 정렬된 원소들은 항상 오름차순을 유지하고 있으므로 위치를 확인할 데이터를 왼쪽으로 한칸씩 이동하다가 자신보다 작은 값을 만났을 경우 멈추게 된다.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):       # index i 부터 0 까지 왼쪽으로 이동하면서 확인한다. 
        if array[j] < array[j-1] :
            array[j], array[j-1] = array[j-1],  array[j]
        else:
            break                   # 자신보다 작은 값을 만나면 멈춤
        
print(array)
            
            
# 시간복잡도 n2