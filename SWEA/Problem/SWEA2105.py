from itertools import combinations_with_replacement as cb
import sys

# Idea Sketch
'''
dfs를 이용한 완전탐색

dfs에는 직사각형의 시작점,가로,세로에대한 정보가 들어간다.

탐색시 시작점으로부터 정해진 방향만큼 순회하며 

'''

sys.stdin = open('SWEA2105', 'r')

# 방향관련 함수


D = ((1, 1), (-1, 1), (-1, -1), (1, -1))


def dfs(s, size, sweets):
    global answer
    # 전역변수로 모든 테스트 케이스에 대해 적용한다.

    x, y = s
    for edge in range(4):
        dx, dy = D[edge]
        if edge % 2 == 0:
            for _ in range(size[0] - 1):
                x, y = x + dx, y + dy
                if x < 0 or y < 0 or x > N - 1 or y > N - 1:
                    # 범위를 벗어나면 리턴하여 종료
                    return
                if board[x][y] in sweets:
                    # 같은 종류인 경우도 리턴하여 종료
                    return
                # 아닌경우 추가하며 순회
                sweets.add(board[x][y])
        else:
            for _ in range(size[1] - 1):
                x, y = x + dx, y + dy
                if x < 0 or y < 0 or x > N - 1 or y > N - 1:
                    return
                if board[x][y] in sweets:
                    return
                sweets.add(board[x][y])
            # 리턴되지 않은 경우 중복이 없으므로 해당 길이를 저장하여 answer와 비교
            # 최대인 경우 저장
    cnt = len(sweets)
    if cnt > answer:
        answer = cnt


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    #
    sizes = list(cb(range(2, N), 2))
    # 격자내에 경로 최대 길이가 N-1에 해당함. diagonal 의 바로 위아래 엔트리.
    sizes.pop()
    for i in range(len(sizes) - 1, -1, -1):
        one, two = sizes[i]
        if one != two:
            sizes.append((two, one))
    sizes.sort(reverse=True)
    answer = -1
    for i in range(N):
        for j in range(N):
            for size in sizes:
                dfs((i, j), size, set())
    print('#%d %d' % (tc, answer))