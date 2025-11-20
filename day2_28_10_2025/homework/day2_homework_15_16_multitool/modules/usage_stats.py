import csv
import os

# usage_stats.csv będzie w folderze z main.py
STATS_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "usage_stats.csv")
)


def load_stats() -> dict[str, int]: # zwraca słownik z kluczem jako stringiem (nazwa programu) i intem jako wartością (liczba uruchomień)
    """Wczytaj statystyki z pliku CSV."""
    stats = {}

    # Plik jeszcze nie istnieje, więc zwracamy pusty
    if not os.path.exists(STATS_FILE):
        return stats

    try:
        with open(STATS_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                # Muszą być dokłądnie 2 kolumny
                if len(row) != 2:
                    continue

                name, count_str = row

                try:
                    stats[name] = int(count_str)
                except ValueError:
                    # Pomijamy jeśli liczba jest "popsuta"
                    continue

    except OSError:
        # Nie udało się odczytać pliku, więc zwracamy pusty
        pass

    return stats


def save_stats(stats: dict[str, int]) -> None:
    """Zapisz statystyki do pliku CSV."""
    try:
        with open(STATS_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            for name, count in stats.items():
                writer.writerow([name, count])
    except OSError:
        print("Nie mogę zapisać statystyk do pliku.")


def increment(name: str) -> None:
    """Zwiększ licznik podanej nazwy o 1."""
    stats = load_stats()

    if name not in stats:
        stats[name] = 0  # domyślna wartość dla nowych programów

    stats[name] += 1

    save_stats(stats)


def get_stats() -> dict[str, int]:
    """Zwróć aktualne statystyki jako zwykły słownik."""
    return load_stats()