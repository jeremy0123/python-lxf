# -*- coding: utf-8 -*-
class Animal(object):
    def run(self):
        print 'Animal is running'

class Dog(Animal):
    #pass
    def run(self):
        super(Dog, self).run() # 注意super的用法
        print 'Dog is running'
    def eat(self):
        print 'Eating meat'

class Cat(Animal):
    pass

d = Dog()
d.run()
d.eat()
c = Cat()
c.run()

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
print isinstance(c, Animal)
