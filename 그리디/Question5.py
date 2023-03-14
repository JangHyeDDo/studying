# 볼링공 고르기

# 서로다른 무게를 고르기
# 볼링공의 개수 n개, 무게는 1~m
# 볼링공 조합

# 먼저 볼링공의 개수와 최대무게, 볼링공의 각 무게를 입력받는다
num, max_weight = map(int, input("볼링공의 개수와 무게 : ").split())
weight = list(map(int,input("볼링공의 무게 : ").split()))

# 볼링공의 각 무게와 최대무게를 비교한다
for i in weight:
    if i > max_weight:
        print("볼링공의 각 무게 다시 설정")
        weight = list(map(int,input("볼링공의 무게 : ").split()))

print("볼링공의 개수는 ",num)
print("볼링공의 최대무게는 ", max_weight)
print("볼링공의 각 무게는 ", weight)

count = 0
new_list = []

# 이중 반복문으로 다른 무게의 볼링공 구하기
for i in weight:
    for j in weight[i:]:
        if i != j:
            new_list.append((i,j))
            count += 1

print("두 사람이 고를 수 있는 경우의 수 : ", count)
print("볼링공의 조합 : ", new_list)
