# Algorytm
# - otwieramy plik
# - wczytujemy z niego liczbę i zwracamy informację ile razy do tej pory był otwarty plik
# - dodajemy +1 do liczby w pliku
# - zapisujemy i zamykamy plik

from modules.counter import opening_counter

# opening_counter(input("Podaj nazwę pliku jaki chcesz sprawdzić (w przypadku braku pliku zostanie stworzony nowy plik): "))
opening_counter("test.txt")