import random2

class Student :

    def __new__(cls, *args, **kwargs):
        print('여기서 우선 메모리에 할당')
        obj = super().__new__(cls)
        return obj


    def __init__(self,index,name):
        print('할당된 객체에 init 수행')
        self.__index=index
        self.__name=name
        self.__english=None
        self.__math=None
        self.__korean=None
        self.__total=None

    def updatetotal(self):
        try :
            self.__total=sum([self.__korean,self.__english,self.__math])
        except :
            pass


    @property
    def kor(self):
        return self.__korean

    @kor.setter
    def kor(self,score):
        try :
            if 101> score>-1 :
                self.__korean=score
                self.updatetotal()

        except :
            pass

    @property
    def eng(self):
        return self.__english
    @eng.setter
    def eng(self,score):
        try :
            if 101> score>-1 :
                self.__english=score
                self.updatetotal()
        except :
            pass

    @property
    def math(self):
        return self.__math
    @math.setter
    def math(self,score):
        try :
            if 101> score>-1 :
                self.__math=score
                self.updatetotal()

        except :
            pass

    def summary(self):
        if self.__total==None :
            print('성적이 입력되지 않았습니다.')
            return
        print(self.__name,'의 성적은 국어 :',self.__korean,' 수학 :',self.__math,' 영어 :',self.__english,'총점 :',self.__total)


H=Student(1,'홍길동')

H.kor='asd'
H.kor=60
H.eng=70
H.math=80
H.summary()


class Duck :

    def __init__(self,idx,name,loc=tuple):
        self.__index=idx
        self.__isred=True
        self.__name=name
        self.__loc=(0,0)

    @property
    def loc(self):
        return self.__loc

    @loc.setter
    def loc(self,loc):
        if type(loc)==tuple :
            try :
                x,y=loc
                self.__loc=(x,y)
            except :
                pass


    def display(self):
        if self.__isred :
            print('Red Duck :',self.__name)
        else :
            print('Mallard Duck :',self.__name)

    def move(self):
        x,y=random2.randint(1,100),random2.randint(1,100)
        self.__loc=self.__loc[0]+x,self.__loc[1]+y
        return

    def sound(self):
        print('cackle')

        return
