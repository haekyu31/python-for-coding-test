# 이진 탐색 소스코드 구현 재귀함수
def binary_search(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) //2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    else:
        return binary_search(array, target, mid + 1, end)