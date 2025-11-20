def adding_elements_to_list() -> list[str]:
    items: list[str] = []
    while True:
        x = input("Podaj element (lub 'k' kończę): ")
        if x.lower() == "k":
            break
        items.append(x)
    return items


def truncate(text: str, width: int = 30) -> str:
    return text if len(text) <= width else text[: width - 3] + "..."


def print_header(width: int, length: int) -> None:
    print("+" + "+".join("-" * width for _ in range(length)) + "+")


def run() -> None:
    print("\n=== Tabela z listy ===")
    items = adding_elements_to_list()
    if not items:
        print("Pusta lista.")
        return

    width = min(max(len(i) for i in items), 30)

    print_header(width, len(items))
    print("|" + "|".join(truncate(i, width).ljust(width) for i in items) + "|")
    print_header(width, len(items))