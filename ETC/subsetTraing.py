


a=[0]*10


def solution(a,n) :
    print(a)



def subset(a,k,n) :

    if k==n :
        solution(a,n)

    else :
        a[k]=0
        subset(a,k+1,n)
        a[k]=1
        subset(a,k+1,n)

print(subset(a,0,10))