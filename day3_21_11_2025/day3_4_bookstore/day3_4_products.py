# produkty
# - książka
# - gazeta
# - ebook
# - komiks

class Product(object):
    def __init__(self, title, page_number, prize):
        self.title = title
        self.page_number = page_number
        self.prize = prize


class Book(Product):
    def __init__(self, title, page_number, prize, year):
        super(Book, self).__init__(title, page_number, prize)
        self.year = year


    def __str__(self):
        return "Książka o tytule {}, liczbie stron {}, cenie {} i roku wydania {}".format(self.title, self.page_number, self.prize, self.year)


class Paper(Product):
    def __str__(self):
        return "Gazeta o tytule {}, liczbie stron {} i cenie {}".format(self.title, self.page_number, self.prize)

class ComicBook(Product):
    def __str__(self):
        return "Komiks o tytule {}, liczbie stron {} i cenie {}".format(self.title, self.page_number, self.prize)
