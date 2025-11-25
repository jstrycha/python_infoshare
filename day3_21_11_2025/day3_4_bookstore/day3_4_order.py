from typing import List

from day3_4_bookstore.day3_4_client import Client
from day3_4_bookstore.day3_4_cart import Cart


class Order(object):
    def __init__(self, client: Client, cart: Cart):
        self.client = client
        self.cart = cart


    def realizuj(self):
        if self.client.wallet > self.cart.value:
            return True
        else:
            print("Nie stać cię, biedaku.")
            return False


    def __str__(self):
        return "Realizuję koszyk dla {}".format(self.client)

