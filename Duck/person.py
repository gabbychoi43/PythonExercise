class Person :
    d='이름'
    def __init__(self):
        self.data=self.d


    @classmethod
    def class_person(cls):
        return cls()

    @staticmethod
    def static_person():
        return Person()

class WhatPerson(Person) :
    d='엄마'

