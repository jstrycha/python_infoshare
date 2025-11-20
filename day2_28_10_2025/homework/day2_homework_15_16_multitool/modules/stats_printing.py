from . import usage_stats


def run() -> None:
    print("\n=== Statystyki użycia Multitoola ===")
    stats = usage_stats.get_stats()

    if not stats:
        print("Brak zapisanych statystyk – jeszcze nic nie uruchamiałeś(aś).")
        return None

    # Wyciągamy licznik samego multitoola
    total_multitool = stats.get("multitool", 0)
    print(f"Multitool uruchomiony łącznie: {total_multitool} razy\n")

    print("Programy:")
    print("------------------------------")
    # Filtrujemy wszystko poza 'multitool'
    for name, count in stats.items():
        if name == "multitool":
            continue
        print(f"- {name}: {count} uruchomienie(-a/-ń)")

    return None