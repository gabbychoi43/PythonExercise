import random

import random2
from abc import *
import turtle



class Duck :
    SIZE = 20
    cnt=1
    def __init__(self):
        self.cnt=Duck.cnt
        Duck.cnt+=1
        self.x=random2.randint(-200,200)
        self.y=random2.randint(-200,200)
        self.turtle=turtle

    @classmethod
    def display(self,turtle):
        return

    def screen_self(self):
        self.turtle.reset()

    def move(self):
        return

    def sound(self):
        print('cackle')

        return


class RedDuck(Duck) :


    def display(self,turtle):
        self.turtle = turtle
        self.turtle.color('#FF0000')
        self.turtle.penup()
        self.turtle.setx(self.x)
        self.turtle.sety(self.y)
        self.turtle.pendown()
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.x+20)
        self.turtle.write(self.cnt)
        self.turtle.setx(self.x+20)
        self.turtle.sety(self.y+20)
        self.turtle.write('quack')
        self.turtle.setx(self.x-20)
        self.turtle.sety(self.y+20)
        self.turtle.pendown()
        self.turtle.write('move',align='right')
        print(self.x,self.y,'redduck')


class MallDuck(Duck) :


    def display(self,turtle):
        self.turtle = turtle
        self.turtle.color('#0000FF')
        self.turtle.penup()
        self.turtle.setx(self.x)
        self.turtle.sety(self.y)
        self.turtle.begin_fill()
        self.turtle.circle(self.SIZE)
        self.turtle.end_fill()
        self.turtle.color('#000000')
        self.turtle.penup()
        self.turtle.setx(self.x+20)
        self.turtle.write(self.cnt)
        self.turtle.setx(self.x+20)
        self.turtle.sety(self.y+20)
        self.turtle.write('quack')
        self.turtle.setx(self.x-20)
        self.turtle.sety(self.y+20)
        self.turtle.pendown()
        self.turtle.write('move',align='right')
        print(self.x,self.y,'mallduck')




class DuckManager :

    def __init__(self):
        self.Ducklist=[]

    def Duckinput(self,du):
        self.Ducklist.append(du)

    def showduck(self):
        for i in self.Ducklist :
            i.display(turtle)


l=[]
DM=DuckManager()

for i in range(10) :

    if random.randint(0,1) :
        DM.Duckinput(RedDuck())
    else :
        DM.Duckinput(MallDuck())

DM.showduck()

input()