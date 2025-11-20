def decimal_to_binary(decimal: int) -> str:
    if decimal == 0:
        return "0"
    bits = ""
    while decimal > 0:
        bits = str(decimal % 2) + bits
        decimal //= 2
    return bits


def binary_to_decimal(b: str) -> int:
    total = 0
    for digit in b:
        if digit not in "01":
            raise ValueError("To nie liczba binarna.")
        total = total * 2 + int(digit)
    return total


def run() -> None:
    print("\n=== Konwerter binarny <-> dziesiętny ===")
    direction = input("Wpisz D (10→2) lub B (2→10): ").strip().upper()

    if direction == "D":
        try:
            n = int(input("Podaj liczbę dziesiętną: "))
        except ValueError:
            print("To nie jest liczba całkowita.")
            return
        print(f"{n} (10) = {decimal_to_binary(n)} (2)")

    elif direction == "B":
        s = input("Podaj liczbę binarną: ")
        try:
            dec = binary_to_decimal(s)
        except ValueError as e:
            print(e)
            return
        print(f"{s} (2) = {dec} (10)")

    else:
        print("Niepoprawna opcja.")