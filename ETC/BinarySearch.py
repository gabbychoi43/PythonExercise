import sys

sys.stdin=open('binary', 'r')

def binarysearch(target,List) :
    left=0
    right=len(List)-1
    while left<=right :
        mid=(left+right)//2
        if List[mid]==target :
            return 1
        if List[mid]>target :
            right=mid-1
        elif List[mid]<target :
            left=mid+1
    return 0



T=int(input())

for t in range(1,T+1) :
    N,M=map(int,input().split())
    A=[int(i) for i in input().split()]
    A=sorted(A)
    B=[int(i) for i in input().split()]
    cnt=0
    for i in B :
        cnt+=binarysearch(i,A)

    print('#%d %d' %(t,cnt))


