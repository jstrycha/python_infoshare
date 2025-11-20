# 12. Napisz program który będzie pamiętnikiem. Niech posiada opcje:
#    - dodawania wpisu do pamiętnika pod określną datą
#    - wyświetlanie wszystkich wpisów z pamiętnika
#    - wyświetlanie wszystkich wpisów dla określonej daty
#    - przeglądanie pojedyńczych wpisów z pamiętnika, opcja: "następny", "poprzedni"

import json
import os

# Plik do którego zapisujemy pamiętnik
DIARY_FILE = "diary.json"

# Baza danych pamiętnika – lista wpisów
diary = []

# ===========================================================================================
# ---------- Funkcje do obsługi pamiętnika ----------
# ===========================================================================================

def load_diary() -> None:
    """Wczytanie pamiętnika z pliku JSON (jeśli istnieje)."""
    global diary  # będziemy zmieniać zmienną globalną - potrzebujemy żeby zmiany były poza funkcją

    if not os.path.exists(DIARY_FILE):
        # Plik nie istnieje – zaczynamy z pustym pamiętnikiem
        diary = [] # upewniamy się, że w diary nie ma żadnych śmieci
        return None

    try:
        with open(DIARY_FILE, "r", encoding="utf-8") as f:
            diary = json.load(f)
            print(f"Wczytano {len(diary)} wpisów z pliku.")
    except (json.JSONDecodeError, OSError):
        print("Nie udało się odczytać pliku z pamiętnikiem. Zaczynamy od pustego.")
        diary = []

    return None


def save_diary() -> None:
    """Zapisanie całego pamiętnika do pliku JSON."""
    try:
        with open(DIARY_FILE, "w", encoding="utf-8") as f:
            json.dump(diary, f, ensure_ascii=False, indent=2) # indent=2 żeby było ładnie
        # print("Pamiętnik zapisany do pliku.")
    except OSError:
        print("Błąd podczas zapisu pliku z pamiętnikiem.")


    return None # pytanie - czy zawsze warto to pisać?


def add_entry() -> None:
    """Dodawanie wpisu do pamiętnika pod określoną datą."""
    print("\n--- Dodawanie wpisu ---")
    date = input("Podaj datę (np. 2025-11-18): ").strip() # data w formacie ISO
    # tu by można się pokusić o branie np. timestampu, ale na potrzeby łatwiejszego testowania bierzemy datę od użytkownika
    # branie daty też można by ulepszyć, bo w tej chwili to nie jest użytkowniko-odporne (może to zrobię jak ogarnę pozostałe zadania do zrobienia :D)

    if not date:
        print("Data nie może być pusta.")
        return None

    print("Wpisz treść wpisu. Zakończ pustą linią:")
    lines = []
    while True:
        line = input()
        if line == "":  # pusta linia przerywa pętlę (kończy wpis)
            break
        lines.append(line)

    text = "\n".join(lines) # tworzymy jednego stringa z wszystkich kolejnych linii

    if not text.strip():
        print("Treść wpisu jest pusta, nic nie zapisano.")
        return None

    entry = {"date": date, "text": text}
    diary.append(entry)

    # Zapisujemy do pliku po dodaniu
    save_diary()

    print("Wpis został dodany i zapisany do pliku.")


def show_all_entries() -> None:
    """
    Wyświetlanie wszystkich wpisów z pamiętnika.
    Nie przyjmuje żadnych argumentów, bo używa globalnej zmiennej diary
    """
    print("\n-------- Wszystkie wpisy --------")
    if not diary: # pusta lista == False, to samo co len(diary) == 0
        print("Pamiętnik jest pusty.")
        return None

    for i, entry in enumerate(diary, start=1): # start=1, bo chcemy wipsy numerować od 1 a nie od 0
        print(f"\nWpis #{i}")
        print(f"Data: {entry['date']}")
        print("Treść:")
        print(entry["text"])
        print("-" * 30)

    return None


def show_entries_for_date() -> None:
    """Wyświetlanie wszystkich wpisów dla podanej daty."""
    print("\n--- Wpisy dla konkretnej daty ---")
    if not diary:
        print("Pamiętnik jest pusty.")
        return

    date = input("Podaj datę (np. 2025-11-18): ").strip()

    found_entries = [e for e in diary if e["date"] == date]

    if not found_entries:
        print(f"Brak wpisów dla daty: {date}")
        return None

    print(f"\nWpisy dla daty {date}:")
    for i, entry in enumerate(found_entries, start=1):
        print(f"\nWpis #{i}")
        print("Treść:")
        print(entry["text"])
        print("-" * 30)

    return None

def browse_entries() -> None:
    """
    Przeglądanie pojedynczych wpisów: następny/poprzedni.
    Zaczynamy od najstarszych wpisów
    """
    print("\n--- Przeglądanie wpisów ---")
    if not diary:
        print("Pamiętnik jest pusty.")
        return None

    # Tworzymy posortowaną listę wpisów według daty
    sorted_entries = sorted(diary, key=lambda e: e["date"])
    index = 0  # zaczynamy od pierwszego wpisu

    while True:
        current = sorted_entries[index]
        print("\n==============================")
        print(f"Wpis {index + 1} z {len(sorted_entries)}")
        print(f"Data: {current['date']}")
        print("Treść:")
        print(current["text"])
        print("==============================")

        print("Opcje:")
        print(" [n] - następny")
        print(" [p] - poprzedni")
        print(" [q] - wyjdź do menu")
        choice = input("Wybierz opcję: ").strip().lower()

        if choice == "n":
            if index < len(sorted_entries) - 1:
                index += 1
            else:
                print("\n==============================")
                print("To jest ostatni wpis.")
        elif choice == "p":
            if index > 0:
                index -= 1
            else:
                print("\n==============================")
                print("To jest pierwszy wpis.")
        elif choice == "q":
            break
        else:
            print("Nieznana opcja. Użyj: n / p / q.")


def main_menu() -> None:
    """Główne menu programu."""

    options = {
        "1": add_entry,
        "2": show_all_entries,
        "3": show_entries_for_date,
        "4": browse_entries,
        "5": None,   # specjalna opcja zakończenia programu
    }

    while True:
        print("\n============ ~~~ PAMIĘTNIK ~~~ ===============")
        print("1. Dodaj wpis")
        print("2. Wyświetl wszystkie wpisy")
        print("3. Wyświetl wpisy dla konkretnej daty")
        print("4. Przeglądaj wpisy (następny/poprzedni)")
        print("5. Zakończ program")

        choice = input("Wybierz opcję (1-5): ").strip()

        if choice in options:
            if choice == "5":
                print("Pa pa pamiętniczku! Do zobaczenia!")
                break
            else:
                action = options[choice]   # pobieramy funkcję ze słownika
                action()                   # wywołujemy ją
        else:
            print("Nieprawidłowy wybór. Wpisz cyfrę 1-5.")


# Uruchomienie programu
if __name__ == "__main__":
    # NOWOŚĆ: przed wejściem do menu próbujemy wczytać pamiętnik z pliku
    load_diary()
    main_menu()
