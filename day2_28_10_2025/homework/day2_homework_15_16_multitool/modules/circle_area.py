PI = 3.1415926535


def run() -> None:
    print("\n=== Pole koła ===")
    try:
        r = float(input("Podaj promień koła (w cm): "))
    except ValueError:
        print("To nie jest liczba.")
        return

    area = PI * r ** 2
    print(f"Pole koła o promieniu {r} cm wynosi {area:.2f} cm²")