import sys

sys.stdin=open('binaryThm','r')


T=int(input())


for t in range(1,T+1) :
    n, a, b = map(int, input().split())
    dp = [[1], [1, 1]]

    for i in range(2, n + 1):
        temp = []
        temp.append(1)
        for j in range(1, i):
            temp.append(dp[i - 1][j - 1] + dp[i - 1][j])
        temp.append(1)
        dp.append(temp)

    print('#%d %d' %(t,dp[n][a]))


