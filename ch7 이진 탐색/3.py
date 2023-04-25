# 부품이 있다면 yes 없다면 no를 순서대로 출력한다. 
n = int(input())
array = [int(i) for i in input().split()]

m = int(input())
li = [int(i) for i in input().split()]

# 문제해결 알고리즘 
# brute force
# for i in range(len(li)):
#     if li[i] in array:
#         print('yes', end = ' ')
#     else:
#         print('no', end = '')
        
# 이진 탐색
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None
for i in li:
    result = binary_search(array, i, 0, n -1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end= ' ')