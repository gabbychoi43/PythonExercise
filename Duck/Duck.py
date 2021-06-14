import random2
import turtle



class Duck :

    def __init__(self,idx,name,loc=tuple):
        self.__index=idx
        self.__name=name
        self.__loc=(0,0)
        self.__turtle=None
        self.__size=20

    @property
    def loc(self):
        return self.__loc

    @loc.setter
    def loc(self,loc):
        try :
            x,y=loc
            self.__loc=(x,y)
        except :
            pass


    def display(self,turtle):
        print(self.__loc,self.__name,self.__size)
        self.__turtle=turtle
        self.__turtle.color('#BBBBff')
        self.__turtle.penup()
        self.__turtle.setx(self.__loc[0])
        self.__turtle.sety(self.__loc[1])
        self.__turtle.pendown()
        self.__turtle.begin_fill()
        self.__turtle.circle(self.__size)
        self.__turtle.end_fill()
        return

    def screen_self(self):
        self.__turtle.reset()

    def move(self):
        x,y=random2.randint(1,100),random2.randint(1,100)
        self.__loc=self.__loc[0]+x,self.__loc[1]+y
        return

    def sound(self):
        print('cackle')

        return

l=[]

for i in range(10) :
    D=Duck(i,'D'+str(i))
    x,y=random2.randint(-200,200),random2.randint(-200,200)
    D.loc=(x,y)
    D.display(turtle)
    l.append(D)

input()

