import sys

sys.stdin=open('11403','r')

N = int(input())

Graph = []
for i in range(N):
    Graph.append([int(i) for i in input().split()])

for i in range(N):
    for j in range(N):
        for k in range(N):
            if Graph[i][k] == 1 and Graph[k][j] == 1:
                Graph[i][j] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            if Graph[i][k] == 1 and Graph[k][j] == 1:
                Graph[i][j] = 1


s=[]
for i in range(N) :
    temp=''
    for k in range(N) :
        temp+=str(Graph[i][k])+' '
    s.append(temp)
for i in range(N) :
    print(s[i])
