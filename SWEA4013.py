import sys

sys.stdin=open('sample_input4013.txt','r')

class Gears() :

    def __init__(self,Gear):
        self.Gear=Gear
        self.rotinfo=[0]*len(Gear)

    def rot(self,gear,dir):
        if dir==1:
            return [gear[len(gear)]]+gear[:len(gear)-1]
        else :
            return gear[1:]+[gear[0]]

    def polardet(self,gear1,gear2,dir):

        return 0


    def Move(self,rotinfo):

        return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Count =int(input())
    Gears =[]
    Rotinfo =[]
    sum =0
    for i in range(4) :
        Gears.append([int(i) for i in input().split()])
    for i in range(Count) :
        a,b=map(int,input().split())
        Rotinfo.append((a,b))



    print("#{}".format(test_case))


