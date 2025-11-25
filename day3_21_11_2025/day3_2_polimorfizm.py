class Animal(object):
    def __init__(self):
        self.is_alive = True
        self.legs = 4


    def say_something(self):
        print('Grrrr')


class Cat(Animal):
    def say_something(self):
        print('Miauuuuu')

class Dog(Animal):
    def say_something(self):
        print('Hauuuuu')

class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__() # super - odwołuje się do klasy nadrzędnej - bez tego nie weźmie metod z klasy rodzica
        self.legs = 0
        self.fin = 'red'


    def say_something(self):
        print('Bul bul')


animals = [Animal(), Dog(), Fish()]

for animal in animals:
    animal.say_something()