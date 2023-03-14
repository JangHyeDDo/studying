# 만들 수 없는 금액

# N개의 동전으로 만들 수 없는 양의 정수 금액 중 최솟값

# 동전을 정렬 후 검사하기
# 근데 덧셈을 해서 최솟값찾기가 워낙 힘든데
# 반복문만 계속 돌리기엔 가성비가 별론데

num = int(input("동전 갯수 : "))
money = list(map(int, input("동전 값 :").split()))

money.sort()
print(f"동전은 {money}")

new_list = []
result = 0

for i in range(len(money)):
    new_list.append(money[i])
    for j in range(i+1, len(money)):
        result = money[i] + money[j]
        new_list.append(result)

new_list.sort()
print(f"동전의 조합은 {new_list}")

# 합한 값들을 비교하면서 없는 작은 수 찾기
for i in range(1,max(new_list)):
    if i not in new_list:
        print(f"만들 수 없는 최솟값은 {i}")
        break