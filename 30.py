# -*-coding: utf-8 -*-

# 多重继承 Mixin混合，类似于Java的interface
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixin(object):
    pass

class FlyableMixin(object):
    pass

class Dog(Mammal, RunnableMixin): # 多重继承
    pass

class Bat(Mammal, FlyableMixin):
    pass
