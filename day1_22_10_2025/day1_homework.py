# 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (niech program zapyta o kierunek konwersji)

# def celsius_to_farenheit(temp_c):
#     temp_f = temp_c * (9 / 5) + 32
#     return temp_f
#
#
# def fahrenheit_to_celsius(temp_f):
#     temp_c = (temp_f - 32) * 5/9
#     return c
#
#
# conversion_type = input("Wybierz czy chcesz przeliczyć temperaturę ze stopni Celsjusza na Fahrenheita (wpisz 'C') czy odwrotnie (wpisz 'F'): ").upper()
# temp = float(input(f"Podaj temperaturę w °{conversion_type}: "))
#
# if conversion_type == 'C':
#     temp_fahr = celsius_to_farenheit(temp)
#     print(f"Temperatura {temp}°{conversion_type} to {temp_fahr:.2f}°F")
# elif conversion_type == 'F':
#     temp_cels = fahrenheit_to_celsius(temp)
#     print(f"Temperatura {temp}°{conversion_type} to {temp_cels:.2f}°F")
# else:
#     print("Nie ma takiej komendy!")

######################################################################################################################################################################

# 2. Napisz program do obliczania pola powierzchni koła o zadanym promieniu (wyświetlając wzór i kolejne obliczenia)

# PI = 3.1415926535
#
# radius = float(input("Podaj promień koła (w cm): "))
#
# print(f"Pole powierzchni koła o promieniu {radius} wynosi {PI * radius**2:.2f} cm^2")
# print(f"Pole powierzchni obliczono jako iloczyn liczby PI (~{PI:.3f}) oraz promienia koła podniesionego do potęgi drugiej (r^2 = {radius**2} cm^2)")

######################################################################################################################################################################

# 3. Napisz program, który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków:
#     | (bok)
#     - (góra/dół)
#     + (wierzchołek)
#     czyli np:
#     +---+
#     |   |
#     |   |
#     +---+

# def print_top_bottom(width):
#     print('+', end='')
#     for i in range(width):
#         print('-', end='')
#     print('+')
#
#
# def print_sides(width):
#     print("|" + ' '* (width) + "|")
#
#
# w = int(input('Podaj szerokość prostokąta: '))
# height = int(input('Podaj wysokość prostokąta: '))
#
# print_top_bottom(w)
# for i in range(height):
#     print_sides(w)
# print_top_bottom(w)

######################################################################################################################################################################
# 4. Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny i odwrotnie (niech program zapyta o kierunek konwersji)

# def decimal_to_binary(decimal):
#     if decimal == 0:
#         return "0"
#     binary = "0"
#     while decimal > 0:
#         decimal = decimal // 2 # dzielenie całkowite przez dwa
#         remainder = decimal % 2 # reszta z dzielenia
#         binary = str(remainder) + binary # zapis od tyłu
#     return binary
#
#
# def binary_to_decimal(bin):
#     dec = 0
#     power = 0
#     bin = str(bin)
#     for digit in reversed(bin):   # odwracamy liczbę, żeby zacząć od ostatniej cyfry
#         if digit == "1":
#             dec += 2 ** power
#         power += 1
#     return dec
#
# conversion_type = input("Jaką liczbę chcesz przekonwertować? Jeśli dziesiętną na binarną wpisz 'd', jeśli binarną na dziesiętną wpisz 'b': ").lower()
# number = int(input("Podaj liczbę jaką chcesz zamienić: "))
#
# if conversion_type == 'd':
#     binary_number = decimal_to_binary(number)
#     print(f"Liczba dziesiętna {number} to binarna liczba {binary_number}")
# elif conversion_type == 'b':
#     decimal_number = binary_to_decimal(number)
#     print(f"Liczba binarna {number} to liczba dziesiętna {decimal_number}")
# else:
#    print("Nieprawidłowy wybór!")

######################################################################################################################################################################
# 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym.

# year = int(input("Podaj jaki rok chcesz sprawdzić: "))

# if year % 400 == 0:
#     print(f"Rok {year} jest rokiem przestępnym.")
# elif year % 100 == 0:
#     print(f"Rok {year} nie jest rokiem przestępnym.")
# elif year % 4 == 0:
#     print(f"Rok {year} jest rokiem przestępnym.")
# elif year % 4 != 0:
#     print(f"Rok {year} nie jest rokiem przestępnym.")
# else:
#     print("Nie podałeś roku!")

# def if_leap_year(year):
#     if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#         return True
#     else:
#         return False
#
#
# user_year =int(input("Podaj jaki rok chcesz sprawdzić: "))
#
# if if_leap_year(user_year):
#     print(f"Rok {user_year} jest rokiem przestępnym.")
# else:
#     print(f"Rok {user_year} nie jest rokiem przestępnym.")


######################################################################################################################################################################
# 6. Napisz program do wyliczania silni dla zadanej liczby

# def factorial(n):
#     fac = 1
#     if n == 0:
#             return 1
#     for i in range(1, n+1):
#         fac = i * fac
#         n += 1
#     return fac
#
# number = int(input("Podaj liczbę dla której chcesz wyliczyć silnię: "))
# print(f"Silnia liczby {number} to {factorial(number)}.")


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# number = int(input("Podaj liczbę dla której chcesz wyliczyć silnię: "))
# print(f"Silnia liczby {number} to {factorial(number)}.")


######################################################################################################################################################################
# 7. Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 wydając ich jak najmniej.

# def money_exchange(amount):
#     coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
#     coins_summary = {}
#
#     for coin in coins:
#         how_many_coin = int(amount // coin)
#         coins_summary[coin] = how_many_coin
#         amount = round(amount - how_many_coin * coin, 2)
#     return coins_summary
#
#
# def non_zero_coins(coins_dict):
#     needed_coins = {}
#     for coin, occurrence in coins_dict.items():
#         if occurrence != 0:
#             needed_coins[coin] = occurrence
#     return needed_coins
#
# user_amount = float(input("Podaj kwotę do rozmienienia: "))
# all_coins = money_exchange(user_amount)
# actually_needed_coins = non_zero_coins(all_coins)
#
# print(f"Żeby rozmienić {user_amount} potrzebujesz: ")
# for coin, occurence in actually_needed_coins.items():
#     print(f"{occurence} monet po {coin}")

######################################################################################################################################################################
# 8. Program rysujący piramidę o określonej wysokości, np dla 3
#         #
#       ###
#     #####


# pyramide_hight = int(input("Podaj wysokość pirmady: "))
#
# for i in range(1,pyramide_hight + 1):
#     print(' ' * (pyramide_hight - i), end='')
#     print('#' * i)

######################################################################################################################################################################
# 9. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
# Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
# Maksymalna szerokość kolumny np 30 znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.


def adding_elements_to_list():
    continue_list = True
    user_list = []

    while continue_list:
        user_input = (input("Podaj nowy element listy (naciśnij 'k' jeśli chcesz zakończyć): ")).lower()

        if user_input == 'k':
            continue_list = False
        else:
            user_list.append(user_input)
    return user_list


def truncate(text: str, width: int = 30):
    text = str(text)
    if len(text) <= width:
        return text
    else:
        return text[:width - 3] + '...'

def print_header_bottom(items_to_print, width):
    print('+', end='')
    for i in items_to_print:
        print('-' * (width) + '+', end='')
    print()

def print_table(items_to_print, max_width=30):
    width = 0
    # Find width of the longest item
    for i in items_to_print:
        if len(str(i)) > width:
            width = len(str(i))

    # Max width = 30
    if width > max_width:
        width = max_width

    # Header
    print_header_bottom(items_to_print, width)

    # Body
    print('|', end='')
    for i in items_to_print:
        cell = truncate(i, width)  # truncate if too long text
        cell = cell.ljust(width)   # align to the left
        print(cell + '|', end='')
    print()  # new line

    # Bottom
    print_header_bottom(items_to_print, width)


list_to_print = adding_elements_to_list()
print_table(list_to_print)

# jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn