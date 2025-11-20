import json
import os
import webbrowser
from datetime import date
from typing import Dict, List, Any


# Nazwa pliku do którego będziemy wszystko zapisywać
FILE_NAME = "tasks.json"

# Dane będą wyglądały tak:
# {
#   "2025-11-18": [
#     {"text": "Zadanie 1", "done": false},
#     {"text": "Zadanie 2", "done": true}
#   ]
# }
#
# czyli
# Dict[
#    str,                  # klucz: data
#    List[                 # lista tasków
#       Dict[              # słownik pojedynczego taska
#          str, Any        # nazwa/opis taska i czy zrobione
#       ]
#    ]
# ]


def load_data() -> Dict[str, List[Dict[str, Any]]]:
    """Ładowanie danych z JSONa (o ile istnieje)."""
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_data(data: Dict[str, List[Dict[str, Any]]]) -> None:
    """Zapisujemy wszystko do JSONa."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_today_date() -> str:
    """Zwracanie obecnej daty w formacie ISO, czyli np. '2025-11-18'."""
    return date.today().isoformat()


def show_tasks(tasks_for_today: List[Dict[str, Any]]) -> None:
    """Drukowanie wszystkich tasków na dany dzień."""
    if not tasks_for_today:
        print("\nImpreza! Żadnych tasków na dziś!\n")
        return None

    print("\nDzisiejsze taski:")
    for i, task in enumerate(tasks_for_today, start=1):
        status = "Zrobione" if task["done"] else "To do dooooo"
        print(f"| {i}. | {status} | {task['text']} |")


def add_task(tasks_for_today: List[Dict[str, Any]]) -> None:
    """Dodawanie nowego taska do listy."""
    text = input("Dodaj opis nowego taska: ").strip()
    if not text:
        print("Task nie może być pusty.")
        return

    tasks_for_today.append({
        "text": text,
        "done": False
    })
    print("Task dodany.")


def mark_task_done(tasks_for_today: List[Dict[str, Any]]) -> None:
    """Oznacz wybrany task jako wykonany."""
    if not tasks_for_today:
        print("Brak tasków do oznaczenia.")
        return None

    show_tasks(tasks_for_today)
    choice = input("Wybierz task do oznaczenia: ")

    if not choice.isdigit():
        print("Podaj numer taska.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(tasks_for_today):
        print("Nie ma takiego taska.")
        return None

    tasks_for_today[index]["done"] = True
    print("Zadanie odhaczone jako wykonane.")
    return None


def delete_task(tasks_for_today: list[dict]) -> None:
    """Usuwanie wybranego taska z listy"""
    if not tasks_for_today:
        print("Brak tasków do usunięcia.")
        return None

    show_tasks(tasks_for_today)
    choice = input("Wybierz numerek taska do usunięcia: ").strip()

    if not choice.isdigit():
        print("Podaj numer.")
        return None

    index = int(choice) - 1

    if index < 0 or index >= len(tasks_for_today):
        print("Nie ma takiego taska.")
        return None

    removed = tasks_for_today.pop(index)
    print(f"Usunięty task: {removed.get('text', '')}")
    return None


def menu() -> str:
    """Wyświetla opcje programu do wyboru."""
    options = {
        "1": "Pokaż taski",
        "2": "Dodaj taski",
        "3": "Oznacz task jako zrobione",
        "4": "Usuń task",
        "5": "Wyjście z programu",
    }

    print("\n========= DZIENNA CHECKLISTA =========")
    for key, label in options.items():
        print(f"{key}. {label}")

    return input("Wybierz opcję (1-5): ").strip()


def exit_program(tasks_for_today: list[dict]) -> None:
    """Wyjście z programu."""
    print("Do zobaczenia!")
    return None

def show_image_from_url(url: str):
    print("\nSprawdź co cię dzisiaj czeka!")
    webbrowser.open(url)

# ===========================================================================================
# ---------- FUNKCJA GŁÓWNA (obsługa wejścia i logika programu) ----------
# ===========================================================================================
def main() -> None:
    """Główna część programu."""
    data = load_data()
    today = get_today_date()

    if today not in data:
        data[today] = []

    tasks_for_today = data[today]

    # Mapowanie możliwych do wykonania akcji
    actions = {
        "1": show_tasks,
        "2": add_task,
        "3": mark_task_done,
        "4": delete_task,
        "5": exit_program,
    }

    show_image_from_url("https://www.cadburydessertscorner.com/hs-fs/hubfs/dc-website-2022/articles/from-pink-cake-guess-who-to-mexican-desserts-pink-panther-characters-as-desserts/from-pink-cake-guess-who-to-mexican-desserts-pink-panther-characters-as-desserts.webp?width=1152&height=648&name=from-pink-cake-guess-who-to-mexican-desserts-pink-panther-characters-as-desserts.webp")

    while True:
        choice = menu()

        action = actions.get(choice)

        if action is None:
            print("INieprawidłowy wybór, spróbuj ponownie.\n")
            continue

        # wywołujemy odpowiednią funkcję
        action(tasks_for_today)

        # jeśli wybrano Exit, zapisujemy dane i wychodzimy z pętli
        if choice == "5":
            save_data(data)
            break

        # po każdej innej akcji zapisujemy dane
        save_data(data)


if __name__ == "__main__":
    main()