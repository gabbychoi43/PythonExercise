import sys

sys.stdin=open('미로탐색', 'r')

from collections import deque

N, M = map(int, input().split())

Map = []
for i in range(N):
    Map.append([int(i) for i in input()])

visited = {}
for i in range(N):
    for j in range(M):
        visited[(i, j)] = False

visited[(0, 0)] = True
visited.values()
q = deque()
q.append([(0, 0), 1])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

F=False
while q:
    if F :
        break
    loc, step = q.popleft()
    x, y = loc
    for i in range(4):

        nx, ny = x + dx[i], y + dy[i]
        if 0<= nx < N and 0 <= ny < M :
            if Map[nx][ny]==1 :
                if not visited[(nx, ny)]:
                    visited[(nx,ny)]=True
                    if nx == N - 1 and ny == M - 1:
                        print(step+1)
                        F=True
                        break
                    q.append([(nx, ny), step + 1])


