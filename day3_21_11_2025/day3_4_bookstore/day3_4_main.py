from day3_4_bookstore.day3_4_cart import Cart
from day3_4_bookstore.day3_4_client import Client
from day3_4_bookstore.day3_4_order import Order
from day3_4_bookstore.day3_4_products import Book, Paper, ComicBook
from day3_4_bookstore.day3_4_address import Address

produkt_1 = Book('Pan Tadeusz', 200, 25.99, 2024)
produkt_2 = Paper('Newsweek', 20, 14)
produkt_3 = ComicBook('Superman', 38, 28228.99)

cart = Cart()
cart.dodaj(produkt_1)
cart.dodaj(produkt_2)
cart.dodaj(produkt_3)
print(cart)

adres_nowak = Address('Firoga', 'Gdańsk')
client = Client(22222222222, 'Jan Nowak', adres_nowak, 1500)
print(client)

order = Order(client, cart)
print(order)
order.realizuj()