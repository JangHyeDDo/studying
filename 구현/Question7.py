# 럭키 스트레이트

# 점수 N (항상 짝수 / 예를 들어 2자리, 4자리, 6자리)
# 자릿수를 나누어 각 합이 같으면 LUCKY 출력
# 자릿수를 나누어 각 합이 다르면 READY 출력

num = list(map(int,input("점수 입력 : ")))

# 길이가 홀수일 경우 다시 입력받기
if len(num) % 2 == 1:
    num = input("점수 입력 : ")

num1 = []
num2 = []

# 반으로 나누어 각각 배열에 넣기
for i in range(len(num)):
    if i < len(num) / 2:
        num1.append(num[i])
    else:
        num2.append(num[i])

answer1 = 0
answer2 = 0

# 각 배열 합 구하기
#for i in range(len(num1)):
#    answer1 += num1[i]
#    answer2 += num2[i]

answer1 = sum(num1)
answer2 = sum(num2)

if answer1 == answer2:
    print("LUCKY")
else:
    print("READY")
