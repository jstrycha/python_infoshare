# koszyk
# - wartość koszyka
# - elementy
from day3_4_bookstore.day3_4_client import Client
from day3_4_bookstore.day3_4_products import Product


class Cart(object):
    def __init__(self):
        self.value = 0
        self.items = []


    def dodaj(self, product: Product):
        self.value += product.prize
        self.items.append(product.title)


    def __str__(self):
        return "W koszyku jest {} produktów o wartości {}". format(len(self.items),self.value)
