class Animal(object):
    def __init__(self):
        self.is_alive = True
        self.legs = 4

# animal_1 = Animal()
# print(animal_1)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

class Fish(Animal):
    def __init__(self):
        super(Fish, self).__init__() # super - odwołuje się do klasy nadrzędnej - bez tego nie weźmie metod z klasy rodzica
        self.legs = 0
        self.fin = 'red'

class Monkey(Animal):
    def __init__(self):
        self.legs = 2


animal = Animal()
dog = Dog()
fish = Fish()
print(animal, dog, fish)
print(animal.legs, dog.legs, fish.legs)
# print(monkey.is_alive) # to się wywali, bo nie dziedziczymy z konstruktora Animal przez brak super