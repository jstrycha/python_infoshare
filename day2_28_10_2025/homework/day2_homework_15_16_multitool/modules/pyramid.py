def run() -> None:
    print("\n=== Piramida ===")
    try:
        h = int(input("Wysokość piramidy: "))
    except ValueError:
        print("Musi być liczba całkowita.")
        return

    if h <= 0:
        print("Wysokość musi być dodatnia.")
        return

    for i in range(1, h + 1):
        print(" " * (h - i) + "#" * (2 * i - 1))