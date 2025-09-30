# 안전지대 
'''지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

제한사항
board는 n * n 배열입니다.
1 ≤ n ≤ 100
지뢰는 1로 표시되어 있습니다.
board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.'''


def solution(board):

    # 몇 행인지 확인
    n = len(board)

    # board copy
    danger = [[0]*n for _ in range(n)]

    # 8방향 (위,아래,좌,우,대각선)
    directions = [(-1,-1)(-1,0)(-1, 1)
                  (0,-1)(0,0)(0,1)
                  (1,-1)(1, 0)(1,1)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:      # 지뢰가 있으면
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n: 
                        danger[nx][ny] = 1
    # 안전지대 개수 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if danger[i][j] == 0:
                safe_count += 1

    return safe_count





    answer = 0
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])) # 16
