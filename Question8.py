# 문자열 재정렬

# 문자열 입력 받기
# 알파벳 오름차순 후 숫자는 합하기

str = input("문자열 입력 :")

result = ""
res = 0

# 반복문으로 숫자인지 영어인지 구분하기
for i in str:
    if i.isdigit():
        res += int(i)
    elif i.isalpha():
        result += i

#오름차순 정렬
result = sorted(result)
result = "".join(result)
result = result.upper()

print(f"{result}{res}")