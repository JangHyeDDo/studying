n = int(input())
number = list(map(int, input().split()))

result = 0      #최종 그룹 수
count = 0       #그룹에 포함된 사람 수

number.sort()

print(number)

for i in number:
    count+=1
    if count >= i:
        result += 1
        count = 0

print(result)