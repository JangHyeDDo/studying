# 문자열 곱하기 혹은 더하기

# 숫자 문자열이 주어질 때 곱하기 혹은 더하기 연산자로 제일 큰 수 구하기

# 0이 나올때는 앞 혹은 뒤 숫자와 더하기
# 0을 제외한 숫자는 곱하기

# 숫자 문자열을 받아서 리스트에 삽입

# 첫번째 숫자는 다음 숫자와 연산

number = list(map(int, input()))
num_list = []

for i in range(len(number)) :
    num_list.append(number[i])

# 숫자 입력 받아서 새로운 리스트에 하나씩 삽입 (문자열 제거)

print(num_list)
length = len(num_list)

result = 0

# 리스트 불러오기, 리스트의 첫번째 값 먼저 비교 후 이후의 값과 연산
# range를 length-1로 한 이유 : 초기부터 다음 숫자와 바로 연산을 실행했기 때문

for i in range(length-1):
    
    if i == 0:    
        if num_list[i] == 0 :
            result = num_list[i] + num_list[i+1]
        else:
            result = num_list[i] * num_list[i+1]

    else:
        if num_list[i+1] == 0 :
            result = result + num_list[i+1]
        else:
            result = result * num_list[i+1]

    print("i =", i ,"/re = ", result)

print("result = ", result)