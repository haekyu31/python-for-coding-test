# https://school.programmers.co.kr/learn/courses/30/lessons/42891
# food_times는 각 음식을 먹는데 필요한 시간이 순서대로 들어있는 배열
# k는 방송이 중단된 시간
# 더 먹을 음식이 없다면 -1

# 문제 해결 알고리즘 
# k까지 걸리는 시간동안 food_time가 0 보다 크다면 1개를 줄이고 시간을 늘리는 식으로 0이라면 다음음식으로만 이동하도록 
        
# 효율성 부분에서 문제가 발생한다.

# 시간 효율성을 해결하기 위해서는 시간이 적게 걸리는 음식부터 확인하는 그리디로 해결가능
# 우선순위 큐를 이용하여 구현

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1) )
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) *length
        length -= 1
        previous = now
        
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_value) % length][1]