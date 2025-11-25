class Ksiazka(object):
    vat = 7 # stała klasowa

    @classmethod
    def change_vat(cls, new_vat):
        cls.vat = new_vat

    def __init__(self, tytul, autor, ilosc_stron=100, cena=19.99):
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.cena = cena
    def __str__(self):
        return f"{self.tytul}, autor: {self.autor}"
    def __len__(self):
        return self.ilosc_stron
    def __add__(self, other):
        if isinstance(other, Ksiazka):
            return self.ilosc_stron + other.ilosc_stron
        else:
            print('Tak naprawdę nie dodałem nic')
            return self.ilosc_stron

    def cena_brutto(self):
        return self.dolicz_vat(self.cena, self.vat)

    @staticmethod
    def dolicz_vat(cena, vat):
        return round(cena * (100 + vat) / 100, 2)

class Ebook(Ksiazka):
    vat = 23
    def __init__(self, tytul, autor):
        super().__init__(autor, tytul)
        self.format = 'pdf'


class Koszyk():
    def __init__(self):
        self.elementy = []
        self.ilosc_elementow = 0
        self.netto = 0
        self.brutto = 0

    def dodaj(self, element):
        self.elementy.append(element)
        self.ilosc_elementow += 1
        self.netto = self.netto + element.cena
        self.brutto = self.brutto + element.cena_brutto()

    def __len__(self):
        return len(self.elementy)

    def wartosc_netto(self):
        return self.netto

    def wartosc_brutto(self):
        return self.brutto

ksiazka_1 = Ksiazka('Potop', 'Sienkiewicz', 300)
ebook_1 = Ebook('Potop', 'Sienkiewicz')

print(ksiazka_1.cena_brutto())
print(ebook_1.cena_brutto())
print(ksiazka_1.vat, ':', ksiazka_1.cena_brutto())

ksiazka_1.change_vat(100)
print(ksiazka_1.vat, ':', ksiazka_1.cena_brutto())