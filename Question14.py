from itertools import permutations

def solution(n, weak, dist):
    leng = len(weak)
    
    # 원형을 일자배열을 두배로 만들어두기
    for i in range(leng):
        weak.append(weak[i]+n) 
    
    # 최소값을 비교하기
    answer = len(dist) + 1
    
    # 탐색할 시작점 설정
    for i in range(leng):
        # 친구를 나열하는 배열 순열 사용
        for friends in list(permutations(dist, len(dist))):
            # 친구 수
            cnt = 1
            # 해당 친구의 점검 마지막 위치
            location = weak[i] + friends[cnt-1]
            #시작점부터 모든 취약 지점을 확인하기
            for index in range(i, i+leng):
                # 점검위치를 벗어나는 경우
                if location < weak[index]:
                    # 새 친구 투입
                    cnt += 1
                    # 투입 불가시 종료
                    if cnt > len(dist):
                        break
                    location = weak[index] + friends[cnt-1]
        answer = min(answer, cnt)
        print(friends,answer)
    # 더이상 비교할 친구수를 넘어서면 -1 출력
    if answer > len(dist):
        return -1
        
    return print(f"취약점검에 투입될 친구 수 : {answer}")

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

solution(n, weak, dist)