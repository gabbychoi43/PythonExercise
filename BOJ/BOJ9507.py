import sys

sys.stdin=open('BOJ9507','r')

T = int(input())

for t in range(T):

    DP = [1, 1, 2, 4] + [0 for i in range(64)]
    N = int(input())

    for i in range(4, N+1):
        DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3] + DP[i - 4]
    print(DP[N])


