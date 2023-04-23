# 퀵 정렬 quick sort
# 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다. 
# 피벗이 숫자를 교환하는 기준
# 피벗을 고르고 왼쪽에서는 피벗보다 큰 수 오른쪽에서는 피벗보다 작은수를 찾아 두 수를 서로 변경한다. 왼쪽과 오른쪽에서 찾는 값의 위치가 서로 엇갈렸을 경우에 피벗의 위치과 가장 작은 값의 위치를 서로 변경한다. 이후 피벗을 기준으로 왼쪽에는 피벗보다 작은수만 오른쪽에는 피벗보다 큰수만 위치하게 된다. 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
            
    quick_sort(array, start, right -1)
    quick_sort(array, right +1, end)
    
quick_sort(array, 0, len(array)-1)
print(array)

# 시간복잡도 nlogn 