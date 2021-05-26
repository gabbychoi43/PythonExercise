

import sys
sys.stdin=open('subsum','r')

def twentyone(array, num):
    if num < 0:
        return
    if len(array) == 0:
        if num == 0:
            yield []
        return
    for solution in twentyone(array[1:], num):
        yield solution
    for solution in twentyone(array[1:], num - array[0]):
        yield [array[0]] + solution
T=int(input())
for t in range(1,T+1) :
    N, target = map(int, input().split())
    Array=[i+1 for i in range(N)]

    print(twentyone(Array,target))


    print('#%d %d' %(t,0))


