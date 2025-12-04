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
# ---------- Klasa licząca podstawowe statystyki (per tekst) ----------
# ============================================================

class TextStatistics:
    """Obiekt liczący wszystkie statystyki analizowanego tekstu."""

    def __init__(self, text: str, case_sensitive: bool = True):
        self.text = text
        self.case_sensitive = case_sensitive

        # Wyniki analizy
        self.num_chars = 0
        self.num_words = 0
        self.num_numbers = 0
        self.num_sentences = 0
        self.num_lowercase_letters = 0
        self.num_punctuation = 0
        self.letters_stats: Counter = Counter()
        self.digits_stats: Counter = Counter()

    # ---------- Funkcje liczące podstawowe statystyki (per plik) ----------

    def count_characters(self) -> int:
        """Zwraca liczbę wszystkich znaków w tekście."""
        self.num_chars = len(self.text)
        return self.num_chars

    def count_words_manual(self) -> int:
        """Zwraca liczbę wyrazów w tekście (ręczne przejście po znakach)."""
        in_word = False
        count = 0

        for ch in self.text:
            if ch.isalnum():        # znak należy do słowa
                if not in_word:
                    count += 1
                    in_word = True
            else:
                in_word = False

        # nie nadpisujemy num_words, tylko zwracamy; możesz użyć jeśli chcesz
        return count

    def count_words_regexp(self) -> int:
        """Zwraca liczbę wyrazów w tekście (podejście z użyciem regexu)."""
        words = re.findall(r"\b\w+\b", self.text, flags=re.UNICODE)
        self.num_words = len(words)
        return self.num_words

    def count_numbers(self) -> int:
        """Zwraca liczbę 'liczb' – ciągów cyfr w tekście."""
        numbers = re.findall(r"\b\d+\b", self.text)
        self.num_numbers = len(numbers)
        return self.num_numbers

    def count_sentences_regexp(self) -> int:
        """
        Liczy zdania zakończone: ., !, ?, ...
        Wielokropek ('...') traktowany jako jeden koniec zdania.
        Jeśli w tekście nie ma żadnego znaku kończącego zdanie, funkcja zwraca 0.
        Pomija segmenty, które nie zawierają żadnych liter ani cyfr.
        """

        # jeśli nie ma żadnego znaku końca zdania – nie liczymy zdań
        if not re.search(r"(?:\.\.\.|[.!?])", self.text):
            self.num_sentences = 0
            return 0

        # Regex dzielący tekst na zdania
        sentences = re.split(r"(?:(?:\.\.\.)|[.!?])(?:\s+|$)", self.text)
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
        self.num_sentences = len(sentences)
        return self.num_sentences

    def count_lowercase_letters(self) -> int:
        """Zwraca liczbę małych liter (wg metody str.islower())."""
        # wyrażenie generatorowe - dla każdego małego znaku dostajemy 1, wszystkie jedynki są sumowane
        self.num_lowercase_letters = sum(1 for char in self.text if char.islower())
        return self.num_lowercase_letters

    def letter_statistics(self) -> Counter:
        """
        Zwraca Counter z liczbą wystąpień poszczególnych liter.
        Jeśli case_sensitive=False – najpierw zamieniamy tekst na małe litery.
        """
        text = self.text if self.case_sensitive else self.text.lower()
        letters = [ch for ch in text if ch.isalpha()]
        self.letters_stats = Counter(letters)
        return self.letters_stats

    def digit_statistics(self) -> Counter:
        """Zwraca Counter z liczbą wystąpień poszczególnych cyfr."""
        digits = [ch for ch in self.text if ch.isdigit()]
        self.digits_stats = Counter(digits)
        return self.digits_stats

    def count_punctuation(self) -> int:
        """Zwraca liczbę znaków interpunkcyjnych."""
        punctuation = set(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        # wyrażenie generatorowe
        self.num_punctuation = sum(1 for ch in self.text if ch in punctuation)
        return self.num_punctuation

    def analyze(self) -> "TextStatistics":
        """Uruchamia wszystkie liczenia, zwraca self dla wygody."""
        self.count_characters()
        self.count_words_regexp()
        self.count_numbers()
        self.count_sentences_regexp()
        self.count_lowercase_letters()
        self.count_punctuation()
        self.letter_statistics()
        self.digit_statistics()
        return self


# ============================================================
# ---------- Klasa licząca statystyki programu ----------
# ============================================================

class ProgramStatistics:
    """
    Statystyki pracy programu zapisane w osobnym pliku.
    Jedna definicja opisuje wszystkie statystyki.
    """

    STAT_DEFS = {
        "runs": "Ilość uruchomień programu",
        "total_chars": "Przeanalizowanych znaków",
        "total_words": "Znalezionych wyrazów",
        "total_numbers": "Znalezionych liczb",
        "total_lowercase_letters": "Znalezionych małych liter",
        "total_punctuation": "Znalezionych znaków interpunkcyjnych",
        "total_sentences": "Znalezionych zdań",
    }

    # key -> etykieta (do zapisu)
    KEY_TO_LABEL = STAT_DEFS
    # etykieta -> key (do odczytu)
    LABEL_TO_KEY = {label: key for key, label in STAT_DEFS.items()}

    def __init__(self, stats_file: str = "program_stats.txt"):
        self.stats_file = stats_file
        # inicjalizacja na podstawie definicji
        self.stats = {key: 0 for key in self.STAT_DEFS}
        self.load_program_stats()

    # ============================================================
    # ---------- Funkcje liczące statystyki programu ----------
    # ============================================================

    def load_program_stats(self) -> dict:
        """
        Ładuje statystyki pracy programu z pliku tekstowego.
        Jeśli plik nie istnieje – zwraca słownik z zerami.
        """
        path = Path(self.stats_file)
        if not path.exists():
            return self.stats

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()  # usuwamy białe znaki
                # jeśli pusta linia albo nie mamy formatu "klucz: wartość" to pomijamy
                if not line or ":" not in line:
                    continue
                key, value = line.split(":", 1)
                key = key.strip()
                value = value.strip()

                stat_key = self.LABEL_TO_KEY.get(key)
                if stat_key is not None:
                    self.stats[stat_key] = int(value)

        return self.stats

    def save_program_stats(self, stats=None) -> None:
        """Zapisuje statystyki pracy programu do pliku tekstowego."""
        if stats is None:
            stats = self.stats

        with open(self.stats_file, "w", encoding="utf-8") as f:
            # zachowujemy kolejność wynikającą z STAT_DEFS
            for key, label in self.KEY_TO_LABEL.items():
                f.write(f"{label}: {stats[key]}\n")

    def update_program_stats(
        self,
        chars: int,
        words: int,
        numbers: int,
        lowercase_letters: int,
        total_punctuation: int,
        sentences: int,
    ) -> dict:
        """Aktualizuje statystyki pracy programu o nowe wartości z jednego uruchomienia."""

        self.stats["runs"] += 1

        increments = {
            "total_chars": chars,
            "total_words": words,
            "total_numbers": numbers,
            "total_lowercase_letters": lowercase_letters,
            "total_punctuation": total_punctuation,
            "total_sentences": sentences,
        }

        for key, value in increments.items():
            self.stats[key] += value

        return self.stats


# ============================================================
# ---------- Klasa spinająca wszystko razem ----------
# ============================================================

class TextAnalyzer:
    """
    Klasa odpowiada za:
    - wczytanie pliku,
    - wykonanie analizy tekstu,
    - aktualizację statystyk programu.
    """

    def __init__(self, stats_file: str = "program_stats.txt"):
        self.stats_file = stats_file

    def analyze_file(self, filename: str, case_sensitive: bool):
        text = read_text_from_file(filename)
        text_stats = TextStatistics(text, case_sensitive=case_sensitive).analyze()

        program_stats_obj = ProgramStatistics(self.stats_file)
        updated_stats = program_stats_obj.update_program_stats(
            chars=text_stats.num_chars,
            words=text_stats.num_words,
            numbers=text_stats.num_numbers,
            lowercase_letters=text_stats.num_lowercase_letters,
            total_punctuation=text_stats.num_punctuation,
            sentences=text_stats.num_sentences,
        )
        program_stats_obj.save_program_stats(updated_stats)

        return text_stats, updated_stats


# ============================================================
# ---------- FUNKCJA GŁÓWNA ----------
# ============================================================

def main():
    # Wybór pliku
    filename = input("Podaj nazwę pliku z tekstem do analizy: ").strip()
    try:
        # sprawdzenie, czy plik istnieje
        _ = read_text_from_file(filename)
    except FileNotFoundError:
        print("Błąd: nie znaleziono pliku.")
        return

    # Pytanie o case sensitivity
    choice = input("Czy analiza liter ma być case sensitive? (t/n): ").strip().lower()
    case_sensitive = (choice == "t")

    analyzer = TextAnalyzer(stats_file="program_stats.txt")
    text_stats, program_stats = analyzer.analyze_file(filename, case_sensitive)

    # Wyświetlenie wyników
    print("\n--- STATYSTYKI TEKSTU ---")

    TEXT_OUTPUT_MAP = {
        "num_chars": "Liczba znaków",
        "num_words": "Liczba wyrazów",
        "num_numbers": "Liczba liczb",
        "num_sentences": "Liczba zdań (szacunkowo)",
        "num_lowercase_letters": "Liczba małych liter",
        "num_punctuation": "Liczba znaków interpunkcyjnych",
    }

    for attr, label in TEXT_OUTPUT_MAP.items():
        print(f"{label}: {getattr(text_stats, attr)}")

    print("\nStatystyka liter:")
    for letter, count in sorted(text_stats.letters_stats.items()):
        print(f"  '{letter}': {count}")

    print("\nStatystyka cyfr:")
    for digit, count in sorted(text_stats.digits_stats.items()):
        print(f"  '{digit}': {count}")

    print("\n--- STATYSTYKA PRACY PROGRAMU (zapisana w program_stats.txt) ---")
    for key, label in ProgramStatistics.KEY_TO_LABEL.items():
        print(f"{label}: {program_stats[key]}")


if __name__ == "__main__":
    main()
