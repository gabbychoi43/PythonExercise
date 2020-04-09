import sys

sys.stdin=open('sample_input2115.txt','r')

class HoneyBee() :
    def __init__(self):
        self


T=int(input())

for test_case in range(1,T+1) :
    solution=0
    N,M,C=map(int,input().split())
    Map=[]
    for i in range(N) :
        Map.append([int(x) for x in input().split()])






    print('#{}'.format(test_case),solution)