# 뱀 문제

# 게임은 n X n 정사각 보드 위에서 진행, 몇몇 칸에 사과가 놓여짐
# 보드의 상하좌우 제일 끝에는 벽이 있음
# 게임 시작시 뱀은 맨 위, 맨 좌측에 위치하고 뱀의 길이 1
# 제일 처음에 오른쪽으로 이동

# 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킴
# 이동한 칸에 사과가 있다면 사과는 사라지고 꼬리는 움직이지 않음
# 이동한 칸에 사과가 없으면 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌, 몸 길이 변화 x

n = int(input("보드의 크기 : "))
k = int(input("사과의 개수 : "))

# 게임 보드판 만들기
board = [[0] * (n+1) for i in range(n+1)]

# 사과의 위치를 0으로 구성된 보드판에 1로 입력
for i in range(k):
    a, b = map(int,input("사과의 위치 : ").split())
    board[a - 1][b - 1] = 1

# 사과가 놓여진 보드 출력하기
for i in board:
    for j in i:
        print(j, end = " ")
    print()

snake_info = []

l = int(input("뱀의 방향 변환 횟수 : "))
# 거리와 방향 입력 받아서 리스트에 삽입
for i in range(l):
    x, c = input("뱀이 이동할 거리와 방향 : ").split()
    snake_info.append((int(x),c))

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def rotate(direction, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전 : 상 -> 우 -> 하 -> 좌 -> 상
    # 왼쪽 회전 : 상 -> 좌 -> 하 -> 우 -> 상
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction+1) % 4

    return direction

def solution():
    direction = 1 #처음에는 우, 오른쪽을 바라봄
    time = 0 #시작한 뒤에 지난 초 시간
    x, y = 1,1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    index = 0 # 회전 정보
    snake = [(x,y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # 보드 안에 있고 몸의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                snake.append((nx,ny))
                px, py = snake.pop(0)
            # 사과가 있다면 이동 후 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                snake.append((nx,ny))
        # 벽이나 몸통에 부딪힌다면
        else:
            time+=1
            break
        
        x,y = nx, ny  # 다음 위치로 이동
        time += 1

        if index <1 and time == snake_info[index][0]: # 회전할 시간일 경우 회전
            direction = rotate(direction, snake[index][1])
            index += 1
        
    return time
     
print(solution())