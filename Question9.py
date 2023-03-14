# 문자열 압축

# 반복되는 문자를 1개 이상의 단위로 압축 -> 짧은 문자열로 표현
# 이후 제일 짧게 압축한 문자열의 길이 return

s = input("문자열을 입력하시오 : ")

# 제한사항 : 문자열 길이 1000 이하 / 소문자
if len(s) > 1000 or not s.islower():
    s = input("문자열을 입력하시오 : ")

# 문자열 길이
result = len(s)

# 반복문, i는 몇 개의 문자를 묶어서 압축할지 반복
for i in range(1,len(s)):
    prev = s[0:i]
    new_str = ""
    cnt = 1
    # prev는 문자 갯수, new_str은 압축한 문자열 저장, cnt는 반복 문자 갯수 
    for j in range(i, len(s), i):
        # s의 문자 prev와 이 다음 문자가 동일시 cnt 증가
        if prev == s[j:j+i]:
            cnt+=1
        # prev와 이 다음 문자가 비동일 시 new_star에 저장
        else:
            new_str += str(cnt) + prev if cnt >= 2 else prev
            prev = s[j:j+i]
            cnt = 1
    
    new_str += str(cnt) + prev if cnt >= 2 else prev

    result = min(result, len(new_str))
    print(f"압축된 문자열 = {new_str}, 길이 = {result}")

print(f"길이는 = {result}")