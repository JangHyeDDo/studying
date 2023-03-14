# 자물쇠와 열쇠

# 자물쇠는 nXn 크기의 정사각형 격자 / 한 칸의  크기가 1
# 특이한 모양의 열쇠는 mXm 크기인 정사각 격자 형태

# 열쇠를 나타내는 2차원 배열 key
# 자물쇠를 나타내는 2차원 배열 lock
# 열쇠의 돌기부분을 자물쇠의 홈부분과 딱 맞게 채우면 자물쇠가 열리는 구조
# 자물쇠 영역 내에서는 열쇠의 돌기부분과 자물쇠의 홈 부분이 정확히 일치
# 열쇠 돌기와 자물쇠 돌기 만날수 없음, 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 함
# 열쇠로 자물쇠로 열 수 있으며 true, 열 수 없으면 false return

# key와 lock는 3과 20사이, 열쇠는 자물쇠보다 작음
# key와 lock 원소는 0과 1로 이루어짐, 0은 홈 부분/1은 돌기 부분

# 처음에는 key 1의 갯수와 lock 0의 갯수 비교
# 회전 또는 이동을 이용하기

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]

def degree (key):
    a = len(key)
    b = len(key[0])

    # 회전할 배열을 0으로 만들기
    new_key = [[0]*a for _ in range(b)]

    for i in range(a):
        for j in range(b):
            # 계산된 배열정보로 90도 회전하기
            new_key[j][a-i-1] = key[i][j]
    return new_key

# 키가 들어간 자물쇠의 값이 전부다 1이면 true
def checking(lock):
    check_length = len(lock) // 3
    for i in range(check_length, check_length*2):
        for j in range(check_length, check_length*2):
            if lock[i][j] != 1:
                return False
    return True

# 자물쇠 푸는 함수
def solution(key, lock):   
    n = len(lock)
    m = len(key)

    # 자물쇠 크기를 크게 해서 비교하기
    new_lock = [[0]*(n*3) for i in range(n*3)]

    # 새로운 자물쇠에 기존 자물쇠 삽입
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    # 90도 180도 270도 360도 돌리기 위해 4번 반복
    for _ in range(4):
        key = degree(key)
        for x in range(n*2):
            for y in range(n*2):
                for a in range(m):
                    for b in range(m):
                        # 자물쇠에 키 값을 삽입
                        new_lock[x+a][y+b] += key[a][b]
                # 홈 키와 돌기값이 맞으면 True
                if checking(new_lock) == True:
                    return True
                # 키 값을 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    
    return False

print(solution(key,lock))
