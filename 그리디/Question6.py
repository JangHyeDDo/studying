# 무지의 먹방 라이브

# 먹어야 할 음식 N개, 1~N번/ 각 음식은 섭취하는데 일정시간 소요
# 1번부터 먹고 번호 증가 순서대로 음식 섭취
# 마지막 번호 음식 먹고 1번 (회전판)
# 음식 하나를 1초동안 섭취
# K초 후에 방송 중단
# 방송 중단 이후 식사 시 몇번 음식?

food_times = list(map(int,input("먹어야 할 음식은? ").split()))
k = int(input("몇초 후 방송 중단? : "))

if len(food_times) != max(food_times):
    food_times = list(map(int,input("먹어야 할 음식은? ").split()))
    k = int(input("몇초 후 방송 중단? : "))

def solution(food_times, k):
    answer = 0
    for i in range(len(food_times)*max(food_times)):    # 초로 돌리기 좋은방법
        if i == k:  
            if i >= len(food_times):
                i -= len(food_times)
                answer = i ##answer = food_times[i]
            break

        if i >= len(food_times):
            i -= len(food_times)
            if food_times[i] == 0:
                pass
            else:
                food_times[i] -= 1
       
        else:
            if food_times[i] == 0:
                pass
            else:
                food_times[i] -= 1

        print(f"i = {i}, result = {food_times}")
    return answer

print(solution(food_times, k))    
