def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def run() -> None:
    print("\n=== Silnia ===")
    try:
        n = int(input("Podaj liczbę całkowitą >= 0: "))
    except ValueError:
        print("To nie jest liczba całkowita.")
        return

    if n < 0:
        print("Liczba musi być >= 0.")
        return

    print(f"{n}! = {factorial(n)}")