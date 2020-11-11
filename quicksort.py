import sys

sys.stdin = open("quick", "r")

def quicksort(List,l,r) :

    if l<r :
        p=partition(List,l,r)
        quicksort(List,l,p-1)
        quicksort(List,p+1,r)

def partition(List,l,r) :
    pivot=(l+r)//2
    while l<r :
        while(List[l]<List[pivot] and  l<r) :
            l+=1
        while (List[r]>=List[pivot] and l<r) :
            r-=1

        if l<r :
            if l==pivot :
                pivot=r
            L[l],L[r]=L[r],L[l]

    L[pivot],L[r]=L[r],L[pivot]
    return r




T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    L=[int(i) for i in input().split()]
    quicksort(L,0,N-1)
    print('#%d %d' %(test_case,L[N//2]))
