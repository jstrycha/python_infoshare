# 15. Stworzenie "programu nakładki" na dotychczasowe programiki.
#    Po wyborze danego programu z "menu" uruchomi się odpowiedni i po wykonaniu danej operacji zapyta czy wykonać inny program.
#    Sugeruje by każdy podprogram był oddzielną funkcją a może nawet modułem.
#    Miejmy na uwadze to by w przyszłości ten program rozwijać podpinając kolejny "podprogram" - powinno to być najprostsze jak się da (np tylko zmiana menu i jakiegoś jednego ifa?:) )
#    Przypominam, że np funkcje można przypisywać do zmiennych.
#    Przykład przy uruchomieniu:
#    "
#    Witaj w Multitool Python Program by Intel - wersja beta ;)
#    Wybierz program który cię interesuje:
#    1) Rysowanie kwadratu o zadanych parametrach
#    2) Rysowanie piramidy o określonej wysokości
#    3) Rozmienianie pieniędzy
#    4) Przeliczanie F->C
#    5) Przeliczanie C->F
#    6) ...
#    7) ...
#    R) Wybierz program losowo bo nie wiem czego szukam:)
#    X) Wyjście z programu
#    Twój wybór: _
#    "

# 16. Dodajcie do multitoola licznik uruchomienia każdego podprogramu i samego multitoola. Dane możecie zapisać w dowolnym pliku CSV/pickle/Excel.
#      Do menu dodajcie pozycję/podprogramik "S - Statystyki" który w przyjaznej formie przedstawi wszystkie statystyki.

import random

from modules import (
    temperature,
    circle_area,
    rectangle_draw,
    binary_converter,
    leap_year,
    factorial_prog,
    money_exchange,
    pyramid,
    table_printer,
    stats_printing,
    usage_stats,
)


def show_menu() -> str:
    """Pokazuje meny programu i pobiera wybór użytkownika."""
    print("\n=== Multitool Python Program – wersja beta ===")
    print("Wybierz program:")
    print("1) Przeliczanie C -> F / F -> C")
    print("2) Pole koła")
    print("3) Rysowanie prostokąta")
    print("4) Konwersja binarny <-> dziesiętny")
    print("5) Sprawdzenie roku przestępnego")
    print("6) Silnia")
    print("7) Rozmienianie pieniędzy")
    print("8) Rysowanie piramidy")
    print("9) Rysowanie tabeli z listy")
    print("S) Statystyki")
    print("R) Wybierz program losowo")
    print("X) Wyjście z programu")
    return input("Twój wybór: ").strip().upper()


def main() -> None:
    """Główna funkcja programu."""

    # funkcje wywoływane po wybraniu odpowiedniej cyfry/litery
    programs = {
        "1": temperature.run,
        "2": circle_area.run,
        "3": rectangle_draw.run,
        "4": binary_converter.run,
        "5": leap_year.run,
        "6": factorial_prog.run,
        "7": money_exchange.run,
        "8": pyramid.run,
        "9": table_printer.run,
        "S": stats_printing.run,
    }

    # nazwy funkcji do statystyk
    program_names = {
        "1": "temperature",
        "2": "circle_area",
        "3": "rectangle",
        "4": "binary_converter",
        "5": "leap_year",
        "6": "factorial",
        "7": "money_exchange",
        "8": "pyramid",
        "9": "table_printer",
        "S": "stats_printing",
    }

    print("Witaj w Multitool Python Program by Intel – wersja beta ;)")

    usage_stats.increment("multitool") #zliczanie uruchomień całego multitoola

    while True:
        choice = show_menu().strip().upper()

        if choice == "R":
            # losujemy program (bez X i R - nie ma ich w programs)
            random_key = random.choice(list(programs.keys()))
            print(f"Losowo wybrany program: {random_key} ({program_names[random_key]})")

            usage_stats.increment(program_names[random_key])
            programs[random_key]()

        else:
            program = programs.get(choice)
            if program is None:
                print("Nie ma takiej opcji, spróbuj ponownie.")
            else:
                usage_stats.increment(program_names[choice])
                program()

        again = input("\nCzy chcesz uruchomić inny program? [T/N]: ").strip().upper()
        if again != "T":
            print("Kończę działanie Multitool. Pa!")
            break


if __name__ == "__main__":
    main()
