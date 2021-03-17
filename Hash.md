# Hash



## No.1 완주하지 못한 선수.

~~~python
def solution(participant, completion):
    temp = 0
    dic = {}
    
    for i in participant :
        dic[hash(i)]=i
        temp=temp+hash(i)
    for j in completion :
        temp=temp-hash(j)
    return dic[temp]
~~~





## No.2 전화번호 목록



~~~python
def solution(phone_book):
    
    phone_book.sort(reverse=True)
    for i in range(len(phone_book)-1) :
        phone_number=phone_book[i]
        prefix_str=phone_book[len(phone_book)-1]
        prefix_len=len(prefix_str)
        if prefix_str==phone_number[:prefix_len] :
            return False
    return True
~~~



## No.3 위장



~~~python
def solution(clothes):
    dic={}
    temp=1
    summ=1
    
    for i in clothes :
        try :
            dic[i[1]].append(i[0])
        except :
            dic[i[1]]=[i[0]]
            
    for i in dic.values() :
        summ*=len(i)+1

    return summ-1
~~~



## No.3 베스트앨범

~~~python
class BestAlbum() :

    def __init__(self,genres,plays):
        self.genres=genres
        self.plays=plays
        self.playrank={}
        self.playtimes=self.makeplaytime()
        self.makeplayrank()
        self.playlist=[]

    def makeplayrank(self):

        for i in range(len(self.genres)) :
            try :
                self.playrank[self.genres[i]]+=self.plays[i]

            except :
                self.playrank[self.genres[i]]=self.plays[i]

    def makeplaytime(self):
        d={}
        for i,j in enumerate(self.genres) :
            try :
                d[j].append((self.plays[i],i))

            except :
                d[j]=[(self.plays[i],i)]

        for i in d :
            d[i].sort(key=lambda x:x[1],reverse=True)
            d[i].sort(key=lambda x:x[0])

        return d

    def makeplaylist(self):

        genreslist=list(self.playrank.keys())
        genreslist.sort(key=lambda x:self.playrank[x],reverse=True)
        print(genreslist)
        for i in genreslist :
            if len(self.playtimes[i])>1 :
                self.playlist.append(self.playtimes[i].pop()[1])
                self.playlist.append(self.playtimes[i].pop()[1])
            else :
                self.playlist.append(self.playtimes[i].pop()[1])


def solution(genres, plays):

    album=BestAlbum(genres,plays)
    album.makeplaylist()


    return album.playlist

~~~

