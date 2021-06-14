class Hello :

    t='상속해줄객체'
    @classmethod
    def calc(self,cls):
        return cls.t

    @staticmethod
    def calc2():
        return Hello.t

    def display(self,x):
        print('display :',x)


class HelloChild(Hello) :
    t='상속받은객체'

print(HelloChild.calc(HelloChild))
print(HelloChild.calc2())





