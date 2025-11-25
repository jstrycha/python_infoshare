from day3_4_bookstore.day3_4_address import Address


class Client(object):
    def __init__(self, nip: int, client_name: str, address: Address, wallet: float):
        self.nip = nip
        self.client_name = client_name
        self.address = address # obiekt klasy Address
        self.wallet = wallet


    def __str__(self):
        return "Klient: {}".format(self.client_name)

