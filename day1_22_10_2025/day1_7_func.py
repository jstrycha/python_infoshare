# def podaj_nazwe_pokolenia():
#     print("Zgaduję nazwę pokolenia")
#
# podaj_nazwe_pokolenia()

def podaj_nazwe_pokolenia(year: int=2000):
    genders_dict = [
        {"from": 2012, "name": "Alpha"},
        {"from": 1946, "to": 1964, "name": "BABY BOOMERS"},
        {"from": 1965, "to": 1980, "name": "X"},
        {"from": 1981, "to": 1996, "name": "Y Milenialsi"},
        {"from": 1997, "to": 2012, "name": "Z"}
    ]

    print('Zgaduje nazwę pokolenia dla roku: ' + str(year))
    nazwa_pokolenia =  ''
    for gender in genders_dict:
        if 'to' in gender:
            if year >= gender['from'] and year <= gender['to']:
                nazwa_pokolenia = gender['name']
                break
        else:
            if year >= gender['from']:
                nazwa_pokolenia = gender['name']
                break

    return nazwa_pokolenia


ask_user = True
while ask_user:
    user_value = input('Podaj rok urodzenia lub wpisz K by zakonczyc program: ')

    if user_value == 'K':
        ask_user = False
    else:
        year = int(user_value)
        nazwa_pokolenia = podaj_nazwe_pokolenia(year)
        print(nazwa_pokolenia)
