import sys

sys.stdin = open('sample_input1953.txt', 'r')


class Arrest():

    def __init__(self, N, M, R, C, L):
        self.Map = {}
        self.N = N
        self.M = M
        self.R = R
        self.C = C
        self.L = L

    def setMap(self, Map):
        for i in range(N):
            for j in range(M):
                self.Map[(i, j)] = {'Object': Map[i][j], 'Visited': False, 'Locable':False}

        self.Map[(self.R, self.C)]['Visited'] = True
        self.Map[(self.R, self.C)]['Locable'] = True

    def Locable(self, Loc, step):
        x, y = Loc
        if step==self.L :
            return 0
        nloc = [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]
        # 0 상 1 하 2 우 3 좌
        Up=[1,2,5,6]
        Down=[1,2,4,7]
        Right=[1,3,6,7]
        Left=[1,3,4,5]

        for i in nloc :
            if i in self.Map :
                if self.Map[Loc]['Object']==1 :
                    self.Map[nloc]

    def Solution(self):

        self.Locable((self.R, self.C),1)
        cnt = 0
        for key, value in self.Map.items():
            if self.Map[key]['Visited'] == True:
                cnt += 1

        return cnt


T = int(input())

for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # N 세로 M 가로 R 세로위치 C 가로위치 L 지난 시간
    Map = []
    for i in range(N):
        Map.append([int(i) for i in input().split()])

    arrest = Arrest(N, M, R, C, L)

    arrest.setMap(Map)

    print('#{}'.format(test_case), arrest.Solution())
