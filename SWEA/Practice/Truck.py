
import sys


sys.stdin = open("SampleTruck", "r")

T = int(input())
for test_case in range(1, T + 1):
    N,M=map(int,input().split())
    container=list(map(int,input().split()))
    Trucks=list(map(int,input().split()))
    container=sorted(container)
    Trucks=sorted(Trucks)
    answer=0
    while True :
        if not Trucks :
            break
        truck=Trucks.pop()

        while container :
            material=container.pop()
            if truck>=material :
                answer+=material
                break
            else :
                continue

    print('#%d %d'%(test_case,answer))
