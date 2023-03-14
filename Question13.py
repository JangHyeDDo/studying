# 치킨 배달

# m개의 치킨집이 남을 경우, 치킨집의 거리 최소값 구하기
# 집 1 치킨집 2

from itertools import combinations

n,m = map(int,input("도시의 크기와 최대 치킨집 개수 : ").split())

chicken = []
house = []

for i in range(n):
    info = list(map(int,input("도시의 정보(1은 집, 2는 치킨집) : ").split()))
    for j in range(n):
        if info[j] == 1:
            house.append([i,j])
        elif info[j] == 2:
            chicken.append([i,j])

print(house)
print(chicken)

def cal(r1,c1,r2,c2):
    result = abs(r1 - r2) + abs(c1 - c2)
    return result

combi = list(combinations(chicken,m))

def getsum():
    answer = 0
    for i in range(len(house)):
        res = 1e9
        for j in range(len(combi)):
            r1, c1 = house[i][0], house[i][1]
            r2, c2 = combi[j][0], combi[j][1]            
            res = min(res, cal(r1,c1,r2,c2))
        answer += res
        print(f"r1,c1 = {r1,c1}, r2,c2 = {r2,c2}, res = {res}")
    
    return answer

answer = 1e9
for combi in combi:
    answer = min(answer, getsum())

print(answer)