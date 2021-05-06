

class knapsack() :


    def __init__(self,weight,value,W):

        self.weight=weight
        self.n=len(weight)
        self.value=value
        self.maxval=0
        self.W=W


    def find(self,W,k,curValue) :
        if W>=0 :
            if k>=self.n :
                if self.maxval<curValue :
                    self.maxval=curValue

            else :
                self.find(W-self.weight[k],k+1,curValue+self.value[k])
                self.find(W,k+1,curValue)




KN=knapsack([5,4,6,3],[10,40,30,50],10)
KN.find(KN.W,0,0)
print(KN.maxval)