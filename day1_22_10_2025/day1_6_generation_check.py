# pokolenie = {
#     range(1929, 1946): "Silent Generation",
#     range(1946, 1965): "Baby Boomers",
#     range(1965, 1980): "X",
#     range(1980,1998): "Y (Millenialsi)",
#     range(1998,2012): "Z",
#     range(2012,2025): "Alfa"
# }
#
# while True:
#     dane_uzytkownika = input("Podaj rok urodzenia ('k' jeśli chcesz zakończyć): ")
#     if dane_uzytkownika == 'k':
#         break
#
#     rok_urodzenia = int(dane_uzytkownika)
#     for lata, nazwa_pokolenia in pokolenie.items():
#         if rok_urodzenia in lata:
#             print(nazwa_pokolenia)
#             break
#     else: #kod wewnątrz bloku else wykona się tylko jeśli pętla nie została przerwana instrukcją brak
#         print("Beta")
#
#
# print("Koniec programu, do widzenia!")


#################################################################################

pokolenie = {
    1946: "Silent Generation",
    1965: "Baby Boomers",
    1980: "X",
    1998: "Y (Millenialsi)",
    2012: "Z",
    2025: "Alfa"
}

while True:
    dane_uzytkownika = input("Podaj rok urodzenia ('k' jeśli chcesz zakończyć): ")
    if dane_uzytkownika == 'k':
        break

    rok_urodzenia = int(dane_uzytkownika)
    for lata, nazwa_pokolenia in pokolenie.items():
        if rok_urodzenia < lata:
            print(nazwa_pokolenia)
            break
    else: #kod wewnątrz bloku else wykona się tylko jeśli pętla nie została przerwana instrukcją brak
        print("Beta")


print("Koniec programu, do widzenia!")
