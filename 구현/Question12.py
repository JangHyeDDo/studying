# 기둥과 보 설치

# 2차원 가상 벽면에 기둥과 보를 이용한 구조물 설치

# 기둥 설치시 우로 한번 가기
# 보 설치시 남으로 한번 가기

n = 5
board = [[0]*(n+1) for i in range(n+1)]

# x = 가로 좌표 y = 세로 좌표 a = 구조물 b = 설치 유무
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],
            #    [5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], 
               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], 
               [1, 1, 1, 0], [2, 2, 0, 1]]

result = []

def solution():
    for i in range(len(build_frame)):
        x, y = build_frame[i][0], build_frame[i][1]
        # a는 구조물의 종류 0:기둥
        a = build_frame[i][2]
        # b는 설치 유무 1이 설치
        b = build_frame[i][3]
        
        # 구조물을 설치할 때
        if b == 1:
            result.append([x,y,a])
            board[x][y] = 1
            if checking(result):
                continue
            else:
                result.remove([x,y,a])
                board[x][y] = 0
        # 구조물을 삭제할 때
        elif b == 0:
            result.remove([x,y,a])
            board[x][y] = 0
            if checking(result):
                continue
            else:
                result.append([x,y,a])
                board[x][y] = 1

    for i in board:
        for j in i:
            print(j, end = " ")
        print()

    return sorted(result)

def checking(result):
    for i in result:
        x,y,a = i
        # 구조물이 기둥 일때
        if a == 0:
            if y == 0 or [x-1,y,1] in result or [x,y-1,0] in result or [x,y,1] in result:
                continue
            else:
                return False
        # 구조물이 보 일때
        elif a == 1:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or [x-1,y,1] in result and [x+1,y,1] in result:
                continue
            else:
                return False
    return True
        
print(solution())
