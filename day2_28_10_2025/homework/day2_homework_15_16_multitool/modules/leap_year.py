def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def run() -> None:
    print("\n=== Rok przestępny ===")
    try:
        year = int(input("Podaj rok: "))
    except ValueError:
        print("Rok musi być liczbą całkowitą.")
        return

    if is_leap_year(year):
        print(f"Rok {year} jest przestępny.")
    else:
        print(f"Rok {year} nie jest przestępny.")