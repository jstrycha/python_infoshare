def money_exchange(amount: float) -> dict[float, int]:
    coins = [5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    result: dict[float, int] = {}

    for coin in coins:
        count = int(amount // coin)
        result[coin] = count
        amount = round(amount - count * coin, 2)

    return result


def run() -> None:
    print("\n=== Rozmienianie pieniędzy ===")
    try:
        amount = float(input("Podaj kwotę: "))
    except ValueError:
        print("To nie wygląda na kwotę.")
        return

    coins = money_exchange(amount)

    print(f"Żeby rozmienić {amount:.2f} zł, potrzebujesz:")
    for coin, count in coins.items():
        if count > 0:
            print(f"  {count} × {coin} zł")