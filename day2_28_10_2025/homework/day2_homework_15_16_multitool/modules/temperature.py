def celsius_to_fahrenheit(temp_c: float) -> float:
    return temp_c * 9 / 5 + 32


def fahrenheit_to_celsius(temp_f: float) -> float:
    return (temp_f - 32) * 5 / 9


def run() -> None:
    print("\n=== Konwerter temperatur C <-> F ===")
    conv = input("Wpisz 'C' jeśli chcesz C -> F, 'F' jeśli F -> C: ").strip().upper()

    if conv not in ("C", "F"):
        print("Nie ma takiej opcji.")
        return

    try:
        temp = float(input(f"Podaj temperaturę w °{conv}: "))
    except ValueError:
        print("To nie wygląda na liczbę.")
        return

    if conv == "C":
        print(f"{temp:.2f}°C = {celsius_to_fahrenheit(temp):.2f}°F")
    else:
        print(f"{temp:.2f}°F = {fahrenheit_to_celsius(temp):.2f}°C")
