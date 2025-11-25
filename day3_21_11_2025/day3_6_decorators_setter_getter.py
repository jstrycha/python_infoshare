class Czlowiek(object):
    def __init__(self):
        self.__ukryte_pole = None

    @property
    def imie(self):
        print("Pobieram wartośc pola")
        return str(self.__ukryte_pole).capitalize()

    @imie.setter
    def imie(self, nowa_wartosc):
        print("Ustawiam wartość pola")
        self.__ukryte_pole = nowa_wartosc


    @imie.deleter
    def imie(self):
        print('Kasuje wartość pola')
        self.__ukryte_pole = None


czlowiek = Czlowiek()
czlowiek.imie  # traktowane jako właściwość - pobieranie
print(czlowiek.imie)
czlowiek.imie = 'Jan' # ustawianie wartości pola
print(czlowiek.imie)
del(czlowiek.imie) # kasowanie wartości pola