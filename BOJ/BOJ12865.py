import sys

sys.stdin=open('BOJ12865','r')

N,K=map(int,input().split())

DP=[0]*(K+1)

for i in range(N) :
    x,y=map(int,input().split())
    if x<=K :
        DP[x]=y
print(DP)
for i in range(K+1) :
    for j in range(K+1) :
        if DP[i-j]!=0 and  i+j<=K :
            DP[i+j]=max(DP[i],DP[i]+DP[j])

print(DP)


korean, english, mathematics, science = 100, 86, 81, 91
def get_max_score(*args) :
    m=-2e9

    for i in args :
        if i>m :
            m=i
    return m

print(get_max_score(korean, english, mathematics, science))

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

print('.jpg'.find('.jpg'))
for i in files :
    if i.find('.jpg')>0 or i.find('.png')>0 :
        print(i)

for i in (list(filter(lambda file: file.find('.jpg')>0 or file.find('.png')>0,files))) :
    print(i)