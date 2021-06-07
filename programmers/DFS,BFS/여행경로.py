import collections
import copy
class Travels() :

    def __init__(self,ticekts):
        self.tickets=ticekts
        self.table=collections.defaultdict(list)
        self. maketable()

    def Journeys(self):
        result=[]
        self.dfs('ICN',self.table,[],result,len(self.tickets))
        return sorted(result)[0]

    def maketable(self):
        for v in self.tickets:
            f,t=v[0],v[1]
            self.table[f].append(t)


    def dfs(self,start,table,arr,result,n_tickets):

        arr.append(start)
        for i in range(len(table[start])) :
            if table[start][i]==True :
                continue
            else :
                next_des=table[start][i]
                table[start][i]=True
                temp=self.dfs(next_des,table,arr,result,n_tickets)
                if len(temp)==n_tickets+1:
                    result.append(copy.deepcopy(temp))

                arr.pop()
                table[start][i]=next_des

        return arr









def solution(tickets):
    travel=Travels(tickets)
    x=travel.Journeys()

    return x