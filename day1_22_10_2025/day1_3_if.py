# condition = True
#
# while condition:
#     input("Podaj liczbę: ")
#     condition = False
#
# ##############################################################################
#
# ile_masz_lat = input('Ile masz lat: ')
# ile_masz_lat = int(ile_masz_lat)
#
# if ile_masz_lat > 40:
#     print('Jesteś bardzo pełnoletni')
# elif ile_masz_lat >= 18:
#     print("Pełnoletni")
# else:
#     print("Małoletni")


############################################################################
while True:
    dane_uzytkownika = input("Podaj rok urodzenia ('k' jeśli chcesz zakończyć): ")
    if dane_uzytkownika == 'k':
        break
    rok_urodzenia = int(dane_uzytkownika)
    if rok_urodzenia >= 1928 and rok_urodzenia <= 1945:
        print('Pokolenie Silent Generation')
    elif rok_urodzenia <= 1964:
        print('Pokolenie Baby Boomers')
    elif rok_urodzenia <= 1980:
        print('Pokolenie  X')
    elif rok_urodzenia <= 1997:
        print('Pokolenie Y (Millenialsi)')
    elif rok_urodzenia <= 2012:
        print('Pokolenie Z')
    else:
       print('Pokolenie Alfa')

print('Koniec programu!')