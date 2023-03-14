# 문자열 뒤집기

# 문자열 검사
# 0과 1로 이루어진 문자열을 입력 받아서
# 0 또는 1로 변경하는데 최소한의 횟수
# ex) 0011001111 -> 111111111 2번

num = input("문자열 입력 :")

if len(num) > 1000000: 
    num = input("문자열 재입력 : ")

count0 = num.count('0')
count1 = num.count('1')
count = 0

if count0 > count1:
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            if num[i+1] == '1':
                count += 1
            else:
                pass

elif count0 < count1:
    for i in range(len(num)-1):
        if num[i] != num[i+1]:
            if num[i+1] == '0':
                count += 1
            else:
                pass

print(count)
