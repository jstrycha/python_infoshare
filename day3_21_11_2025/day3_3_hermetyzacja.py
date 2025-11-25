class Animal(object):
    def __init__(self):
        self.is_alive = True
        self.legs = 4
        self._almost_private = 'almost_private'
        self.__almost_private = 'private'


    def __str__(self):
        return 'Animal with {} legs. Still alive? {}'.format(self.legs, self.is_alive)

    def amputation(self, legs):
        if legs >= self.legs:
            self.is_alive = False
            self.legs = 0
        else:
            self.legs -= legs


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

    def amputation(self, legs):
        print('Nice try :)')

    def say_something(self):
        print('Bul bul')


dog = Dog()
print(dog)
dog.amputation(3)
print(dog)
dog.amputation(3)

fish = Fish()
print(fish)
fish.amputation(3)
print(fish)

animal = Animal()
print(animal._almost_private)
# print(animal.__private) # to nie zadziała
print(animal._Animal__almost_private) # ale jak już dodamy nazwę klasy to niestety już zadziała

