import abc
import random
from abc import abstractmethod
import abc
import turtle

class Duck(metaclass=abc.ABCMeta) :



    __instance=None
    CNT=1
    SIZE=30
    def __init__(self):
        self.__x=random.randint(-300,300)
        self.__y=random.randint(-300,300)
        self.CNT+=1


    def getxy(self):
        return self.__x,self.__y


    @abstractmethod
    def display(self) :
        pass


    def swim(self):
        return '수영'



class FlyThing :


    def Fly(self):
        return 'Flying'

class SoundThing :

    @abstractmethod
    def quack(self):
        pass


class mallardDuck(Duck,SoundThing,FlyThing) :
    color='#0000FF'
    def __init__(self):
        super(mallardDuck, self).__init__()
        self.__myShape='Mallard'
        self.__x,self.__y=self.getxy()
        self.cnt=self.CNT

    def display(self) :
        self.turtle = turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setx(self.__x)
        self.turtle.sety(self.__y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.__x+20)
        self.turtle.write(self.swim())
        self.turtle.setx(self.__x+20)
        self.turtle.sety(self.__y+20)
        self.turtle.write(self.quack())
        self.turtle.setx(self.__x-20)
        self.turtle.sety(self.__y+20)
        self.turtle.pendown()
        self.turtle.write(self.Fly(),align='right')
        print(self.__x,self.__y,'redduck')


    def quack(self):
        return '꽥꽥'




class display() :

    def display(self):

        self.turtle = turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setx(self.__x)
        self.turtle.sety(self.__y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.__x+20)
        self.turtle.write(self.swim())
        self.turtle.setx(self.__x+20)
        self.turtle.sety(self.__y+20)
        self.turtle.write(self.quack())
        self.turtle.setx(self.__x-20)
        self.turtle.sety(self.__y+20)
        self.turtle.pendown()
        self.turtle.write(self.Fly(),align='right')
        print(self.__x,self.__y,'redduck')




class RedDuck(Duck,SoundThing,FlyThing) :
    color='#FF0000'

    def __init__(self):
        super(RedDuck, self).__init__()
        self.__myShape='Red'
        self.__x,self.__y=self.getxy()
        self.cnt=self.CNT

    def display(self):

        self.turtle = turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setx(self.__x)
        self.turtle.sety(self.__y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.__x+20)
        self.turtle.write(self.swim())
        self.turtle.setx(self.__x+20)
        self.turtle.sety(self.__y+20)
        self.turtle.write(self.quack())
        self.turtle.setx(self.__x-20)
        self.turtle.sety(self.__y+20)
        self.turtle.pendown()
        self.turtle.write(self.Fly(),align='right')
        print(self.__x,self.__y,'redduck')



    def quack(self):
        return '꽥꽥'


class RubberDuck(Duck,SoundThing) :
    color='#FFFF00'

    def __init__(self):
        super(RubberDuck, self).__init__()
        self.__myShape='Orange'
        self.__x,self.__y=self.getxy()
        self.cnt=self.CNT

    def display(self):

        self.turtle = turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setx(self.__x)
        self.turtle.sety(self.__y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.__x+20)
        self.turtle.write(self.quack())
        self.turtle.setx(self.__x+20)
        self.turtle.sety(self.__y+20)
        self.turtle.write(self.swim())
        self.turtle.setx(self.__x-20)
        self.turtle.sety(self.__y+20)
        self.turtle.pendown()
        print(self.__x,self.__y,self.__myShape)

    def quack(self):
        return '삑삑'

class DecoyDuck(Duck) :
    color='#00FF00'

    def __init__(self):
        super(DecoyDuck, self).__init__()
        self.__myShape='GREEN'
        self.__x,self.__y=self.getxy()
        self.cnt=self.CNT

    def display(self):

        self.turtle = turtle
        self.turtle.color(self.color)
        self.turtle.penup()
        self.turtle.setx(self.__x)
        self.turtle.sety(self.__y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.__x+20)
        self.turtle.setx(self.__x+20)
        self.turtle.sety(self.__y+20)
        self.turtle.write(self.swim())

        self.turtle.setx(self.__x-20)
        self.turtle.sety(self.__y+20)
        self.turtle.pendown()
        print(self.__x,self.__y,self.__myShape)




class DuckManager :

    __Ducklist = []
    __instance=None

    def __init__(self):
        if not DuckManager.__instance :
            print('creation Instance')
        else :
            print('already')
    @classmethod
    def getInstance(cls):
        if not cls.__instance :
            cls.__instance=DuckManager()
        return cls.__instance


    def makeducks(self,N=int):
        for i in range(N) :
            x=random.randint(0,3)

            if x==0 :
                self.__Ducklist.append(RedDuck())
            elif x==1 :
                self.__Ducklist.append(mallardDuck())
            elif x==2 :
                self.__Ducklist.append(RubberDuck())
            elif x==3 :
                self.__Ducklist.append(DecoyDuck())

    def showducks(self):
        for i in self.__Ducklist :
            print(i)
            i.display()




D2=DuckManager.getInstance()
print(D2)
D2.makeducks(10)
D2.showducks()