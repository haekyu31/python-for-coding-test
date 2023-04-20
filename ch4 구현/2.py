# n이 입력되면 00시 00분 00초부터 n시 59분 59초까지 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

h = int(input())

# 숫자를 문자로 바꿔서 3이 들어가는지 확인하기
# brute force 문제

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)