# 0과 1로만 이루어진 문자열 S 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 방법 모두 같은 숫자로 바꾸어야 한다.

# 문제해결 알고리즘 
# 결과는 0 또는 1로 만들기 0으로 만들경우와 1로 만들경우를 생각 
# 연속된 숫자 갯수를 가지고 나누어서 바꾸어야 하는 부분을 생각

n = input()

num_1 = [num for num in n.split('1') if num]
num_0 = [num for num in n.split('0') if num]

print(min(len(num_1), len(num_0)))