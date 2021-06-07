import math

L=[520,498,481,512,515,542,520,518,527,526]

n=sum(L)/len(L)

V=0
for i in L :
    V+=(i-n)**2

V*=(1/(len(L)-1))

print(n,V,math.sqrt(V))

x=math.sqrt(9)

delta=(2.262)*math.sqrt(V)/x
print(delta)

N=(-delta+n,delta+n)
print(N)