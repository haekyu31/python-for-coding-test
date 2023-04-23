# 성적이 낮은 순서대로 학생의 이름을 출력

n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key=lambda x: x[1])

for student in array:
    print(student[0], end=' ')
