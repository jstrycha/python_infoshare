# 10. Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak, np:
# ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
# Niech będzie możliwość wyboru tryb case sensitivity.
# Niech program tworzy też plik ze statystyką swojej pracy. Czyli np:
# " Ilość uruchomień programu: 10
# Przeanalizowanych znaków: 1223435991
# Znalezionych wyrazów: 2399
# Znalezionych liczb: 122
# Znalezionych małych liter: 68923455 etc "
#
# Oczywiście dopuszalna jest ułomność takiego programu.
# Dokładne policzenie ilość zdań nie jest trywialne ale może jakiś fajny algorytm uda się Wam wymyślić.
# Rodzaje statystyk zostawiam waszej fantazji :)
# Przydatny generator tekstu: http://lipsum.pl/

import re
import string
from collections import Counter
from pathlib import Path

# ============================================================
# ---------- Funkcja wczytująca dane z pliku ----------
# ============================================================

def read_text_from_file(filename: str) -> str:
    """Wczytuje cały tekst z pliku."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

# ============================================================
# ---------- Funkcje liczące podstawowe statystyki (per plik) ----------
# ============================================================

def count_characters(text: str) -> int:
    """Zwraca liczbę wszystkich znaków w tekście."""
    return len(text)


def count_words_manual(text: str) -> int:
    """Zwraca liczbę wyrazów w tekście (ręczne przejście po znakach)."""
    in_word = False
    count = 0

    for ch in text:
        if ch.isalnum():        # znak należy do słowa
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    return count


def count_words_regexp(text: str) -> int:
    """Zwraca liczbę wyrazów w tekście (podejście z użyciem regexu)."""
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    return len(words)


def count_numbers(text: str) -> int:
    """Zwraca liczbę 'liczb' – ciągów cyfr w tekście."""
    numbers = re.findall(r"\b\d+\b", text)
    return len(numbers)


def count_sentences_regexp(text: str) -> int:
    """
    Liczy zdania zakończone: ., !, ?, ...
    Wielokropek ('...') traktowany jako jeden koniec zdania.
    Jeśli w tekście nie ma żadnego znaku kończącego zdanie, funkcja zwraca 0.
    Pomija segmenty, które nie zawierają żadnych liter ani cyfr.
    """

    # jeśli nie ma żadnego znaku końca zdania – nie liczymy zdań
    if not re.search(r"(?:\.\.\.|[.!?])", text):
        return 0

    # Regex dzielący tekst na zdania
    sentences = re.split(r"(?:(?:\.\.\.)|[.!?])(?:\s+|$)", text)
    # (?:...) - grupa nieskładowana - grupuje, nie zapisuje numeru grupy
    #   (?:\.\.\.)|[.!?] - co kończy zdanie
    #       - \.\.\. - wielokropek
    #       - [.!?] - lub jeden z tych znaków
    #   (?:\s+|$) - co jest po końcu zdania
    #       - \s - dowolny biały znak (spacja, tabulator, \n itp.)
    #       - + - 1 lub więcej
    #       - $ - koniec tekstu
    # Usuwanie pustych lub "niefrazowych" segmentów (bez liter/cyfr)
    sentences = [
        s for s in sentences
        if s.strip() and any(ch.isalpha() or ch.isdigit() for ch in s)
    ]
    return len(sentences)


def count_lowercase_letters(text: str) -> int:
    """Zwraca liczbę małych liter (wg metody str.islower())."""
    # wyrażenie generatorowe - dla każdego małego znaku dostajemy 1, wszystkie jedynki są sumowane
    return sum(1 for char in text if char.islower())


def letter_statistics(text: str, case_sensitive: bool = True) -> Counter:
    """
    Zwraca Counter z liczbą wystąpień poszczególnych liter.
    Jeśli case_sensitive=False – najpierw zamieniamy tekst na małe litery.
    """
    if not case_sensitive:
        text = text.lower()
    letters = [ch for ch in text if ch.isalpha()]
    return Counter(letters)


def digit_statistics(text: str) -> Counter:
    """Zwraca Counter z liczbą wystąpień poszczególnych cyfr."""
    digits = [ch for ch in text if ch.isdigit()]
    return Counter(digits)


def count_punctuation(text: str) -> int:
    """Zwraca liczbę znaków interpunkcyjnych."""
    punctuation = set(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    # wyrażenie generatorowe
    return sum(1 for ch in text if ch in punctuation)

# ============================================================
# ---------- Funkcje liczące statystyki programu ----------
# ============================================================

def load_program_stats(stats_file: str) -> dict:
    """
    Ładuje statystyki pracy programu z pliku tekstowego.
    Jeśli plik nie istnieje – zwraca słownik z zerami.
    """
    default_stats = {
        "runs": 0,
        "total_chars": 0,
        "total_words": 0,
        "total_numbers": 0,
        "total_lowercase_letters": 0,
        "total_punctuation": 0,
        "total_sentences": 0,
    }

    path = Path(stats_file)
    if not path.exists():
        return default_stats

    # tworzymy kopię, żeby nie nadpisać zerowych wartości w default_stats
    stats = default_stats.copy()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()  # usuwamy białe znaki
            # jeśli pusta linia albo nie mamy formatu "klucz: wartość" to pomijamy
            if not line or ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            # klucze w pliku dopasowujemy do naszych
            if key == "Ilość uruchomień programu":
                stats["runs"] = int(value)
            elif key == "Przeanalizowanych znaków":
                stats["total_chars"] = int(value)
            elif key == "Znalezionych wyrazów":
                stats["total_words"] = int(value)
            elif key == "Znalezionych liczb":
                stats["total_numbers"] = int(value)
            elif key == "Znalezionych małych liter":
                stats["total_lowercase_letters"] = int(value)
            elif key == "Znalezionych znaków interpunkcyjnych":
                stats["total_punctuation"] = int(value)
            elif key == "Znalezionych zdań":
                stats["total_sentences"] = int(value)

    return stats


def save_program_stats(stats_file: str, stats: dict) -> None:
    """Zapisuje statystyki pracy programu do pliku tekstowego."""
    with open(stats_file, "w", encoding="utf-8") as f:
        f.write(f"Ilość uruchomień programu: {stats['runs']}\n")
        f.write(f"Przeanalizowanych znaków: {stats['total_chars']}\n")
        f.write(f"Znalezionych wyrazów: {stats['total_words']}\n")
        f.write(f"Znalezionych liczb: {stats['total_numbers']}\n")
        f.write(f"Znalezionych małych liter: {stats['total_lowercase_letters']}\n")
        f.write(f"Znalezionych znaków interpunkcyjnych: {stats['total_punctuation']}\n")
        f.write(f"Znalezionych zdań: {stats['total_sentences']}\n")


def update_program_stats(
    stats: dict,
    chars: int,
    words: int,
    numbers: int,
    lowercase_letters: int,
    total_punctuation: int,
    sentences: int,
) -> dict:
    """Aktualizuje statystyki pracy programu o nowe wartości z jednego uruchomienia."""
    stats["runs"] += 1
    stats["total_chars"] += chars
    stats["total_words"] += words
    stats["total_numbers"] += numbers
    stats["total_lowercase_letters"] += lowercase_letters
    stats["total_punctuation"] += total_punctuation
    stats["total_sentences"] += sentences
    return stats

# ============================================================
# ---------- FUNKCJA GŁÓWNA ----------
# ============================================================

def main():
    # Wybór pliku
    filename = input("Podaj nazwę pliku z tekstem do analizy: ").strip()
    try:
        text = read_text_from_file(filename)
    except FileNotFoundError:
        print("Błąd: nie znaleziono pliku.")
        return

    # Pytanie o case sensitivity
    choice = input("Czy analiza liter ma być case sensitive? (t/n): ").strip().lower()
    case_sensitive = (choice == "t")

    # Obliczenia – każde przez osobną funkcję
    num_chars = count_characters(text)
    num_words = count_words_regexp(text)
    num_numbers = count_numbers(text)
    num_sentences = count_sentences_regexp(text)
    num_lowercase = count_lowercase_letters(text)
    letters_stats = letter_statistics(text, case_sensitive=case_sensitive)
    digits_stats = digit_statistics(text)
    num_punctuation = count_punctuation(text)

    # Wyświetlenie wyników
    print("\n--- STATYSTYKI TEKSTU ---")
    print(f"Liczba znaków: {num_chars}")
    print(f"Liczba wyrazów: {num_words}")
    print(f"Liczba liczb: {num_numbers}")
    print(f"Liczba zdań (szacunkowo): {num_sentences}")
    print(f"Liczba małych liter: {num_lowercase}")
    print(f"Liczba znaków interpunkcyjnych: {num_punctuation}")

    print("\nStatystyka liter:")
    for letter, count in sorted(letters_stats.items()):
        print(f"  '{letter}': {count}")

    print("\nStatystyka cyfr:")
    for digit, count in sorted(digits_stats.items()):
        print(f"  '{digit}': {count}")

    # Statystyka pracy programu
    stats_file = "program_stats.txt"
    stats = load_program_stats(stats_file)
    stats = update_program_stats(
        stats,
        chars=num_chars,
        words=num_words,
        numbers=num_numbers,
        lowercase_letters=num_lowercase,
        total_punctuation=num_punctuation,
        sentences=num_sentences,
    )
    save_program_stats(stats_file, stats)

    print("\n--- STATYSTYKA PRACY PROGRAMU (zapisana w program_stats.txt) ---")
    print(f"Ilość uruchomień programu: {stats['runs']}")
    print(f"Przeanalizowanych znaków: {stats['total_chars']}")
    print(f"Znalezionych wyrazów: {stats['total_words']}")
    print(f"Znalezionych liczb: {stats['total_numbers']}")
    print(f"Znalezionych małych liter: {stats['total_lowercase_letters']}")
    print(f"Znalezionych znaków interpunkcyjnych: {stats['total_punctuation']}")
    print(f"Znalezionych zdań: {stats['total_sentences']}")


if __name__ == "__main__":
    main()
