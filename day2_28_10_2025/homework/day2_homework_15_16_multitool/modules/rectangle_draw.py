def print_top_bottom(width: int) -> None:
    print("+" + "-" * width + "+")


def print_sides(width: int, height: int) -> None:
    for _ in range(height):
        print("|" + " " * width + "|")


def run() -> None:
    print("\n=== Rysowanie prostokąta ===")
    try:
        w = int(input("Podaj szerokość: "))
        h = int(input("Podaj wysokość: "))
    except ValueError:
        print("Muszą być liczby całkowite.")
        return

    if w <= 0 or h <= 0:
        print("Wymiary muszą być dodatnie.")
        return

    print_top_bottom(w)
    print_sides(w, h)
    print_top_bottom(w)